# Science Fiction Novel API - Bottle Edition
#
# Adapted from "Creating Web APIs with Python and Flask"
# <https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask>.
#

import sys
import textwrap
import logging.config
import sqlite3

import bottle
from bottle import get, post, error, abort, request, response, HTTPResponse
from bottle.ext import sqlite

# Set up app, plugins, and logging
#
app = bottle.default_app()
app.config.load_config('./etc/api.ini')

plugin = sqlite.Plugin(app.config['sqlite.dbfile'])
app.install(plugin)

logging.config.fileConfig(app.config['logging.config'])


# Return errors in JSON
#
# Adapted from # <https://stackoverflow.com/a/39818780>
#
def json_error_handler(res):
    if res.content_type == 'application/json':
        return res.body
    res.content_type = 'application/json'
    if res.body == 'Unknown Error.':
        res.body = bottle.HTTP_CODES[res.status_code]
    return bottle.json_dumps({'error': res.body})


app.default_error_handler = json_error_handler

# Disable warnings produced by Bottle 0.12.19.
#
#  1. Deprecation warnings for bottle_sqlite
#  2. Resource warnings when reloader=True
#
# See
#  <https://docs.python.org/3/library/warnings.html#overriding-the-default-filter>
#
if not sys.warnoptions:
    import warnings
    for warning in [DeprecationWarning, ResourceWarning]:
        warnings.simplefilter('ignore', warning)


# Simplify DB access
#
# Adapted from
# <https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/#easy-querying>
#
def query(db, sql, args=(), one=False):
    cur = db.execute(sql, args)
    rv = [dict((cur.description[idx][0], value)
          for idx, value in enumerate(row))
          for row in cur.fetchall()]
    cur.close()

    return (rv[0] if rv else None) if one else rv


def execute(db, sql, args=()):
    cur = db.execute(sql, args)
    id = cur.lastrowid
    cur.close()

    return id


# Routes

@get('/')
def home():
    return textwrap.dedent('''
        <h1>Distant Reading Archive</h1>
        <p>A prototype API for distant reading of science fiction novels.</p>\n
    ''')


@get('/books/')
def books(db):
    all_books = query(db, 'SELECT * FROM books;')

    return {'books': all_books}


@get('/books')
def search(db):
    sql = 'SELECT * FROM books'

    columns = []
    values = []

    for column in ['author', 'published', 'title']:
        if column in request.query:
            columns.append(column)
            values.append(request.query[column])

    if columns:
        sql += ' WHERE '
        sql += ' AND '.join([f'{column} = ?' for column in columns])

    logging.debug(sql)
    books = query(db, sql, values)

    return {'books': books}


@post('/books/')
def create_book(db):
    book = request.json

    if not book:
        abort(400)

    posted_fields = book.keys()
    required_fields = {'published', 'author', 'title', 'first_sentence'}

    if not required_fields <= posted_fields:
        abort(400, f'Missing fields: {required_fields - posted_fields}')

    try:
        book['id'] = execute(db, '''
            INSERT INTO books(published, author, title, first_sentence)
            VALUES(:published, :author, :title, :first_sentence)
            ''', book)
    except sqlite3.IntegrityError as e:
        abort(409, str(e))

    response.status = 201
    response.set_header('Location', f"/books/{book['id']}")
    return book


@get('/books/<id:int>')
def retrieve_book(id, db):
    book = query(db, 'SELECT * FROM books WHERE id = ?', [id], one=True)
    if not book:
        abort(404)

    return {'books': [book]}
