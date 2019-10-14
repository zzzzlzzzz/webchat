from typing import Dict

from flask import Blueprint, Flask, g
from flask_restful import Api
from .post import Post
from .user import User


def pull_user(endpoint: str, values: Dict[str, str]) -> None:
    try:
        g.user = values.pop('username')
    except KeyError:
        g.user = None


def init_app(app: 'Flask') -> None:
    """Initialize API v1"""
    api = Api()
    api.add_resource(Post, 'post')
    api.add_resource(User, 'user')
    bp = Blueprint('api_v1', __name__, url_prefix='/api/v1/<username>/')
    bp.url_value_preprocessor(pull_user)
    api.init_app(bp)
    app.register_blueprint(bp)
