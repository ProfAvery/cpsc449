#!/usr/bin/env python3

import sys
import logging.config

import bottle
from bottle import get, post, request, response, template, redirect


# Set up app and logging
app = bottle.default_app()
app.config.load_config('./etc/app.ini')

logging.config.fileConfig(app.config['logging.config'])

KV_URL = app.config['sessions.kv_url']

# Disable Resource warnings produced by Bottle 0.12.19 when reloader=True
#
# See
#  <https://docs.python.org/3/library/warnings.html#overriding-the-default-filter>
#
if not sys.warnoptions:
    import warnings
    warnings.simplefilter('ignore', ResourceWarning)


@get('/')
def show_form():
    count = request.get_cookie('count', default='0')

    count = int(count) + 1
    response.set_cookie('count', str(count))

    return template('counter.html', counter=count)


@post('/reset')
def reset_count():
    response.delete_cookie('count')

    return redirect('/')
