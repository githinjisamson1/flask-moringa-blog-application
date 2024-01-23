from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from config import bcrypt

# metadata
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# instatiate SQLAlchemy
db = SQLAlchemy(metadata=metadata)


# !USER MODEL
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

    # !password hashing/validation
    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        # utf-8 encoding and decoding is required in python 3
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))

    # username validation
    @validates("username")
    def validate_username(self, key, username):
        if not username:
            raise ValueError("Username required!")

        else:
            if username in [user.username for user in User.query.all()]:
                raise ValueError("Username already in use!")
            return username

    # email validation
    @validates("email")
    def validate_email(self, key, email):
        import re
        pattern = r"^[a-z]*.[a-z]*@student.moringaschool.com"
        regex = re.compile(pattern)

        if not email:
            raise ValueError("Email required!")

        else:
            if not regex.fullmatch(email):
                raise ValueError("Invalid Moringa School email!")
            return email

    # full_name validation
    @validates("full_name")
    def validate_full_name(self, key, full_name):
        if not full_name:
            raise ValueError("Full Name required!")
        return full_name

    # representation
    def __repr__(self):
        return f'''User {self.username} {self.email} {self.full_name}'''


# !COMMENT MODEL
class Comment(db.Model, SerializerMixin):
    __tablename__ = "comments"

    # serialize to prevent recursion
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

    # content validation
    @validates("content")
    def validate_content(self, key, content):
        if not content:
            raise ValueError("Comment required!")

        else:
            if len(content) < 25:
                raise ValueError(
                    "Comment must be at least 25 characters long!")
            return content

    # representation
    def __repr__(self):
        return f'''Comment {self.content} '''


# !VOTE MODEL
class Vote(db.Model, SerializerMixin):
    __tablename__ = "votes"

    # serialize to prevent recursion
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


# !POST MODEL
class Post(db.Model, SerializerMixin):
    __tablename__ = "posts"

    # serialize to prevent recursion
    serialize_rules = ("-comments.post", "-votes.post",)

    # columns
    id = db.Column(db.Integer, primary_key=True)
    phase = db.Column(db.Integer)
    # preview = db.Column(db.String, nullable=False)
    # minutes_to_read = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    resources = db.Column(db.String)
    created_at = db.column(db.DateTime, server_default=db.func.now())
    updated_at = db.column(db.DateTime, onupdate=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # relationships
    comments = db.relationship("Comment", back_populates="post")
    votes = db.relationship("Vote", back_populates="post")

    # phase validation
    @validates("phase")
    def validate_phase(self, key, phase):
        if phase not in range(6):
            raise ValueError("Phase must be either 0, 1, 2, 3, 4, 5")
        return phase

    # content validation
    @validates("content")
    def validate_content(self, key, content):
        if not content:
            raise ValueError("Content required!")

        else:
            if len(content) < 300:
                raise ValueError(
                    "Content must be at least 300 characters long!")
            return content

    # title validation
    @validates("title")
    def validate_title(self, key, title):
        if not title:
            raise ValueError("Title required!")

        else:
            if len(title) not in range(3, 100):
                raise ValueError(
                    "Title must range between 3 and 100 characters long!")
            return title

    # representation
    def __repr__(self):
        return f'''Post {self.phase} {self.preview} {self.minutes_to_read} {self.title} {self.content} {self.resources}'''
