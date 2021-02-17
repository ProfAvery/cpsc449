#!/usr/bin/env python3

import flask
from flask import render_template, session, redirect, url_for

import sessions


app = flask.Flask(__name__)
app.config.from_envvar('APP_CONFIG')

if app.config.get('USE_SESSION_STORE'):
    session_store = sessions.KeyValueSessionStore(
        app.config['KV_URL'],
        logger=app.logger
    )
    app.session_interface = sessions.ServerSideSessionInterface(session_store)


@app.route('/')
def show_form():
    count = session.get('count', 0)

    count += 1
    session['count'] = count

    return render_template('counter.html', counter=count)


@app.route('/reset', methods=['POST'])
def reset_count():
    session.clear()
    return redirect(url_for('show_form'))
