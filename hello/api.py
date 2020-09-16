#!/usr/bin/env python3

# $ http POST 127.0.0.1:5000/greet first_name=Prof last_name=Avery

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/greet', methods=['POST'])
def return_greeting():
    data = request.get_json()

    full_name = f"{data['first_name']} {data['last_name']}"
    app.logger.debug(full_name)

    return jsonify({
        'name': full_name
    })
