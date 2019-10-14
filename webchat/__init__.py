from os import environ
from flask import Flask


def create_app() -> 'Flask':
    """Create flask application

    :return: Flask application instance
    """
    app = Flask(__name__)
    app.config.from_object(environ.get('WEBCHAT_CONFIG', 'config.ProductionConfig'))
    return app
