from os import environ

from flask import Flask, current_app, send_from_directory

from . import api
from .ext import db


def react_app(file):
    """Return React APP from static folder
    In production we send file directly from nginx!

    :param file: Requested file name
    :return: Requested file
    """
    return send_from_directory(current_app.static_folder, file)


def create_app() -> 'Flask':
    """Create flask application

    :return: Flask application instance
    """
    app = Flask(__name__, static_url_path='/frontend')
    app.config.from_object(environ.get('WEBCHAT_CONFIG', 'config.ProductionConfig'))
    db.init_app(app)
    app.add_url_rule('/', 'index', react_app, methods=('GET', ), defaults={'file': 'index.html'})
    app.add_url_rule('/<path:file>', 'index', react_app, methods=('GET', ))
    api.v1.init_app(app)
    return app
