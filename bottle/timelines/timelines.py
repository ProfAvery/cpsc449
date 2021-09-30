import sys
import logging.config

import bottle
from bottle import get, post, request, response, abort
from bottle.ext import sqlite

# Set up app, plugins, and logging
app = bottle.default_app()
app.config.load_config("./etc/timelines.ini")

plugin = sqlite.Plugin(app.config["sqlite.dbfile"])
app.install(plugin)

logging.config.fileConfig(app.config["logging.config"])


# Return errors in JSON
#
# Adapted from <https://stackoverflow.com/a/39818780>
#
def json_error_handler(res):
    if res.content_type == "application/json":
        return res.body
    res.content_type = "application/json"
    if res.body == "Unknown Error.":
        res.body = bottle.HTTP_CODES[res.status_code]
    return bottle.json_dumps({"error": res.body})


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
        warnings.simplefilter("ignore", warning)


# Simplify DB access
#
#
# Adapted from
# <https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/#easy-querying>
#
def query(db, sql, args=(), one=False):
    cur = db.execute(sql, args)
    rv = [
        dict((cur.description[idx][0], value) for idx, value in enumerate(row))
        for row in cur.fetchall()
    ]
    cur.close()

    return (rv[0] if rv else None) if one else rv


def execute(db, sql, args=()):
    cur = db.execute(sql, args)
    id = cur.lastrowid
    cur.close()

    return id


# Routes


@get("/<username>/home")
def getHomeTimeline(username):
    logging.debug("getHomeTimeline(%r)", username)
    return {"timeline": []}


@get("/")
def getPublicTimeline():
    logging.debug("getPublicTimeline()")
    return {"timeline": []}


@get("/<username>/")
def getUserTimeline(username):
    logging.debug("getUserTimeline(%r)", username)
    return {"timeline": []}


@post("/<username>/")
def postTweet(db, username):
    tweet = request.json

    if not tweet:
        abort(400)

    logging.debug("postTweet(%r, %r)", username, tweet["text"])
    response.status = 201
