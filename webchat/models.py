from datetime import datetime

from .ext import db


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    visited = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    posts = db.relationship('Post', back_populates='user', cascade='all, delete-orphan', passive_deletes=True)

    def __init__(self, username: str):
        self.username = username


class Post(db.Model):
    __tablename__ = 'post'

    message_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', back_populates='posts')
    message = db.Column(db.String(1024), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
