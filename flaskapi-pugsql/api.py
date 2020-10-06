# Science Fiction Novel API from "Creating Web APIs with Python and Flask"
# <https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask>.
#
# What's new:
#
#  * Switched from Flask to Flask API
#    <https://www.flaskapi.org>
#
#  * Switched to PugSQL for database access
#    <https://pugsql.org>
#
#  * SQLAlchemy Database URL specified in app config file
#
#  * Adds CLI command to create initial schema from "Using SQLite 3 with Flask"
#    <https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/>
#
#  * New API calls:
#    - GET /api/v1/resources/books/{id} to retrieve a specific book
#    - POST /api/v1/resources/books to create a new book
#

import flask_api
from flask import request
from flask_api import status, exceptions
import pugsql


app = flask_api.FlaskAPI(__name__)
app.config.from_envvar('APP_CONFIG')

queries = pugsql.module('queries/')
queries.connect(app.config['DATABASE_URL'])


@app.cli.command('init')
def init_db():
    with app.app_context():
        db = queries.engine.raw_connection()
        with app.open_resource('books.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def all_books():
    all_books = queries.all_books()

    return list(all_books)


@app.route('/api/v1/resources/books/<int:id>', methods=['GET'])
def book(id):
    book = queries.book_by_id(id=id)
    if book:
        return book
    else:
        raise exceptions.NotFound()


@app.route('/api/v1/resources/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        return filter_books(request.args)
    elif request.method == 'POST':
        return create_book(request.data)


def create_book(book):
    posted_fields = {*book.keys()}
    required_fields = {'published', 'author', 'title', 'first_sentence'}

    if not required_fields <= posted_fields:
        message = f'Missing fields: {required_fields - posted_fields}'
        raise exceptions.ParseError(message)
    try:
        book['id'] = queries.create_book(**book)
    except Exception as e:
        return { 'error': str(e) }, status.HTTP_409_CONFLICT

    return book, status.HTTP_201_CREATED, {
        'Location': f'/api/v1/resources/books/{book["id"]}'
    }


def filter_books(query_parameters):
    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        raise exceptions.NotFound()

    query = query[:-4] + ';'

    results = queries.engine.execute(query, to_filter).fetchall()

    return list(map(dict, results))
