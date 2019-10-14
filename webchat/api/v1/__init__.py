from flask import Blueprint, Flask
from flask_restful import Api
from .post import Post
from .user import User


def init_app(app: 'Flask') -> None:
    """Initialize API v1"""
    api = Api()
    api.add_resource(Post, '<username>/post')
    api.add_resource(User, '<username>/user')
    bp = Blueprint('api_v1', __name__, url_prefix='/api/v1/')
    api.init_app(bp)
    app.register_blueprint(bp)
