from typing import Dict
from datetime import datetime

from flask import Blueprint, Flask, g
from flask_restful import Api
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from .post import Post
from .user import User
from webchat import models
from webchat.ext import db


def pull_user(endpoint: str, values: Dict[str, str]) -> None:
    try:
        username = values.pop('username')
        user_query = models.User.query.filter_by(username=username)
        try:
            with db.session.begin_nested():
                db.session.add(models.User(username))
        except IntegrityError:
            user_query.update({models.User.visited: datetime.utcnow()})
        db.session.commit()
        g.user = user_query.one()
    except (KeyError, NoResultFound):
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
