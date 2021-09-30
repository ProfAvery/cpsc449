# Science Fiction Novel API - Hug Edition
#
# Adapted from "Creating Web APIs with Python and Flask"
# <https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask>.
#

import configparser
import logging.config

import hug
import sqlite_utils

# Load configuration
#
config = configparser.ConfigParser()
config.read("./etc/api.ini")
logging.config.fileConfig(config["logging"]["config"], disable_existing_loggers=False)


# Arguments to inject into route functions
#
@hug.directive()
def sqlite(section="sqlite", key="dbfile", **kwargs):
    dbfile = config[section][key]
    return sqlite_utils.Database(dbfile)


@hug.directive()
def log(name=__name__, **kwargs):
    return logging.getLogger(name)


# Routes
#
@hug.get("/books/")
def books(db: sqlite):
    return {"books": db["books"].rows}


@hug.post("/books/", status=hug.falcon.HTTP_201)
def create_book(
    response,
    published: hug.types.number,
    author: hug.types.text,
    title: hug.types.text,
    first_sentence: hug.types.text,
    db: sqlite,
):
    books = db["books"]

    book = {
        "published": published,
        "author": author,
        "title": title,
        "first_sentence": first_sentence,
    }

    try:
        books.insert(book)
        book["id"] = books.last_pk
    except Exception as e:
        response.status = hug.falcon.HTTP_409
        return {"error": str(e)}

    response.set_header("Location", f"/books/{book['id']}")
    return book


@hug.get("/books/{id}")
def retrieve_book(response, id: hug.types.number, db: sqlite):
    books = []
    try:
        book = db["books"].get(id)
        books.append(book)
    except sqlite_utils.db.NotFoundError:
        response.status = hug.falcon.HTTP_404
    return {"books": books}


@hug.get(
    "/search",
    examples=[
        "published=2017",
        "author=Heinlein",
        "title=Star",
        "first_sentence=night",
    ],
)
def search(request, db: sqlite, logger: log):
    books = db["books"]

    conditions = []
    values = []

    if "published" in request.params:
        conditions.append("published = ?")
        values.append(request.params["published"])

    for column in ["author", "title", "first_sentence"]:
        if column in request.params:
            conditions.append(f"{column} LIKE ?")
            values.append(f"%{request.params[column]}%")

    if conditions:
        where = " AND ".join(conditions)
        logger.debug('WHERE "%s", %r', where, values)
        return {"books": books.rows_where(where, values)}
    else:
        return {"books": books.rows}
