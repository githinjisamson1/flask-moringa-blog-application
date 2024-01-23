from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class User(db.Model):
    __tablename__ = "users"

    # columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    full_name = db.Column(db.String, nullable=False)
    created_at = db.column(db.DateTime, server_default=db.func.now())
    _password_hash = db.Column(db.String, unique=True, nullable=False)

    # representation
    def __repr__(self):
        return f'''User {self.username} {self.email} {self.full_name}'''


class Comment(db.Model):
    __tablename__ = "comments"

    # columns
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    created_at = db.column(db.DateTime, server_default=db.func.now())
    updated_at = db.column(db.DateTime, onupdate=db.func.now())
    user_id = db.Column(db.String, db.ForeignKey("users.id"))
    post_id = db.Column(db.String, db.ForeignKey("posts.id"))

    # representation
    def __repr__(self):
        return f'''Comment {self.content} '''


class Vote(db.Model):
    __tablename__ = "votes"

    # columns
    id = db.Column(db.Integer, primary_key=True)
    vote_type = db.Column(db.Boolean)
    created_at = db.column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))

    # representation
    def __repr__(self):
        return f'''Vote {self.vote_type}'''


class Post(db.Model):
    __tablename__ = "posts"

    # columns
    id = db.Column(db.Integer, primary_key=True)
    phase = db.Column(db.Integer, nullable=False)
    preview = db.Column(db.String, nullable=False)
    minutes_to_read = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    resources = db.Column(db.String, nullable=False)
    created_at = db.column(db.DateTime, server_default=db.func.now())
    updated_at = db.column(db.DateTime, onupdate=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # representation
    def __repr__(self):
        return f'''Post {self.phase} {self.preview} {self.minutes_to_read} {self.title} {self.content} {self.resources}'''
