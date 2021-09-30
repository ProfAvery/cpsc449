import flask
from flask import request, jsonify, g
import sqlite3

app = flask.Flask(__name__)
app.config.from_envvar("APP_CONFIG")


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(app.config["DATABASE"])
        db.row_factory = make_dicts
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.route("/<string:username>/home")
def getHomeTimeline(username):
    app.logger.debug("getHomeTimeline(%r)", username)
    return jsonify([])


@app.route("/", methods=["GET"])
def getPublicTimeline():
    app.logger.debug("getPublicTimeline()")
    return jsonify([])


def getUserTimeline(username):
    app.logger.debug("getUserTimeline(%r)", username)


def postTweet(username, text):
    app.logger.debug("postTweet(%r, %r)", username, text)


@app.route("/<string:username>/", methods=["GET", "POST"])
def userTimeline(username):
    if request.method == "GET":
        getUserTimeline(username)
        return jsonify([]), 200
    elif request.method == "POST":
        json = request.get_json()
        if json and "text" in json:
            postTweet(username, json["text"])
            return jsonify(), 201
        else:
            return jsonify(), 400
