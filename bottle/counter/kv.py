# Simple persistent key-value store
#
# Inspired by <https://docs.repl.it/misc/database>
#

import sys
import shelve
import logging.config

import bottle
from bottle import request, get, put, delete, abort

# Set up app and logging
app = bottle.default_app()
app.config.load_config('./etc/kv.ini')

logging.config.fileConfig(app.config['logging.config'])


# Make sure that each route has bottle.local.db set
def shelf(callback):
    def wrapper(*args, **kwargs):
        with shelve.open(app.config['shelve.dbmfile']) as db:
            bottle.local.db = db
            body = callback(*args, **kwargs)
            bottle.local.db = None
        return body
    return wrapper


app.install(shelf)


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

# Disable Resource warnings produced by Bottle 0.12.19 when reloader=True
#
# See
#  <https://docs.python.org/3/library/warnings.html#overriding-the-default-filter>
#
if not sys.warnoptions:
    import warnings
    warnings.simplefilter('ignore', ResourceWarning)


# http PUT localhost:5100 foo=bar
@put('/')
def set_key():
    req = request.json
    if not req:
        abort(400)
    db = bottle.local.db
    for key in req.keys():
        db[key] = req[key]
    return req

# http localhost:5100/foo
@get('/<key>')
def get_key(key):
    db = bottle.local.db
    return {key: db.get(key)}

# http DELETE localhost:5100/foo
@delete('/<key>')
def delete_key(key):
    db = bottle.local.db
    return {key: db.pop(key, None)}


# http localhost:5100
# http localhost:5100?prefix=f
@get('/')
def match():
    db = bottle.local.db
    keys = db.keys()
    prefix = request.query.get('prefix')
    if prefix:
        matches = [k for k in keys if k.startswith(prefix)]
    else:
        matches = list(keys)
    return {'keys': matches}
