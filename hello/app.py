#!/usr/bin/env python3

# See <https://code-maven.com/using-templates-in-flask>

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def show_form():
    return render_template('form.html')


@app.route('/greet', methods=['POST'])
def show_greeting():
    full_name = f"{request.form['first_name']} {request.form['last_name']}"
    app.logger.debug(full_name)

    return render_template('form.html', name=full_name)
