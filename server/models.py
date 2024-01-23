from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# instatiate SQLAlchemy
db = SQLAlchemy(metadata=metadata)


# !MODELS

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    # serialize to prevent recursion
    serialize_rules = ("-posts.user", "-comments.user", "-votes.user",)

    # columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    full_name = db.Column(db.String, nullable=False)
    created_at = db.column(db.DateTime, server_default=db.func.now())
    _password_hash = db.Column(db.String, unique=True, nullable=False)

    # relationships
    posts = db.relationship("Post", backref="user")
    comments = db.relationship("Comment", back_populates="user")
    votes = db.relationship("Vote", back_populates="user")

    # representation

    def __repr__(self):
        return f'''User {self.username} {self.email} {self.full_name}'''


class Comment(db.Model, SerializerMixin):
    __tablename__ = "comments"

    serialize_rules = ("-user.comments", "-post.user",)

    # columns
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    created_at = db.column(db.DateTime, server_default=db.func.now())
    updated_at = db.column(db.DateTime, onupdate=db.func.now())
    user_id = db.Column(db.String, db.ForeignKey("users.id"))
    post_id = db.Column(db.String, db.ForeignKey("posts.id"))

    # relationships
    user = db.relationship("User", back_populates="comments")
    post = db.relationship("Post", back_populates="comments")

    # representation
    def __repr__(self):
        return f'''Comment {self.content} '''


class Vote(db.Model, SerializerMixin):
    __tablename__ = "votes"

    serialize_rules = ("-user.votes", "-post.votes",)

    # columns
    id = db.Column(db.Integer, primary_key=True)
    vote_type = db.Column(db.Boolean)
    created_at = db.column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))

    # relationships
    user = db.relationship("User", back_populates="votes")
    post = db.relationship("Post", back_populates="votes")

    # representation
    def __repr__(self):
        return f'''Vote {self.vote_type}'''


class Post(db.Model, SerializerMixin):
    __tablename__ = "posts"

    serialize_rules = ("-comments.post", "-votes.post",)

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

    # relationships
    comments = db.relationship("Comment", back_populates="post")
    votes = db.relationship("Vote", back_populates="post")

    # representation
    def __repr__(self):
        return f'''Post {self.phase} {self.preview} {self.minutes_to_read} {self.title} {self.content} {self.resources}'''
