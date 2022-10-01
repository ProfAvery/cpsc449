# Science Fiction Novel API - Quart Edition
#
# Adapted from "Creating Web APIs with Python and Flask"
# <https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask>.
#

import collections
import dataclasses
import sqlite3
import textwrap

import databases
import toml

from quart import Quart, g, request, abort
from quart_schema import QuartSchema, RequestSchemaValidationError, validate_request

app = Quart(__name__)
QuartSchema(app)

app.config.from_file(f"./etc/{__name__}.toml", toml.load)


@dataclasses.dataclass
class Book:
    published: int
    author: str
    title: str
    first_sentence: str


# Database connections on demand
#   See <https://flask.palletsprojects.com/en/2.2.x/patterns/sqlite3/>
#   and <https://www.encode.io/databases/connections_and_transactions/>


async def _get_db():
    db = getattr(g, "_sqlite_db", None)
    if db is None:
        db = g._sqlite_db = databases.Database(app.config["DATABASES"]["URL"])
        await db.connect()
    return db


@app.teardown_appcontext
async def close_connection(exception):
    db = getattr(g, "_sqlite_db", None)
    if db is not None:
        await db.disconnect()


@app.route("/", methods=["GET"])
def index():
    return textwrap.dedent(
        """
        <h1>Distant Reading Archive</h1>
        <p>A prototype API for distant reading of science fiction novels.</p>\n
        """
    )


@app.route("/books/all", methods=["GET"])
async def all_books():
    db = await _get_db()
    all_books = await db.fetch_all("SELECT * FROM books;")

    return list(map(dict, all_books))


@app.route("/books/<int:id>", methods=["GET"])
async def one_book(id):
    db = await _get_db()
    book = await db.fetch_one("SELECT * FROM books WHERE id = :id", values={"id": id})
    if book:
        return dict(book)
    else:
        abort(404)


@app.errorhandler(404)
def not_found(e):
    return {"error": "The resource could not be found"}, 404


@app.route("/books/", methods=["POST"])
@validate_request(Book)
async def create_book(data):
    db = await _get_db()
    book = dataclasses.asdict(data)
    try:
        id = await db.execute(
            """
            INSERT INTO books(published, author, title, first_sentence)
            VALUES(:published, :author, :title, :first_sentence)
            """,
            book,
        )
    except sqlite3.IntegrityError as e:
        abort(409, e)

    book["id"] = id
    return book, 201, {"Location": f"/books/{id}"}


@app.errorhandler(RequestSchemaValidationError)
def bad_request(e):
    return {"error": str(e.validation_error)}, 400


@app.errorhandler(409)
def conflict(e):
    return {"error": str(e)}, 409


SearchParam = collections.namedtuple("SearchParam", ["name", "operator"])
SEARCH_PARAMS = [
    SearchParam(
        "author",
        "LIKE",
    ),
    SearchParam(
        "published",
        "=",
    ),
    SearchParam(
        "title",
        "LIKE",
    ),
    SearchParam(
        "first_sentence",
        "LIKE",
    ),
]


@app.route("/books/search", methods=["GET"])
async def search():
    query_parameters = request.args

    sql = "SELECT * FROM books"
    conditions = []
    values = {}

    for param in SEARCH_PARAMS:
        if query_parameters.get(param.name):
            if param.operator == "=":
                conditions.append(f"{param.name} = :{param.name}")
                values[param.name] = query_parameters[param.name]
            else:
                conditions.append(f"{param.name} LIKE :{param.name}")
                values[param.name] = f"%{query_parameters[param.name]}%"

    if conditions:
        sql += " WHERE "
        sql += " AND ".join(conditions)

    app.logger.debug(sql)

    db = await _get_db()
    results = await db.fetch_all(sql, values)

    return list(map(dict, results))
