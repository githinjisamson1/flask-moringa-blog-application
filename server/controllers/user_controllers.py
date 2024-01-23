from flask import Blueprint, make_response, jsonify
from flask_restful import Api, Resource, reqparse
from server.models import User, Comment, Vote, Post
from server.config import bcrypt, db

user_bp = Blueprint("user_bp", __name__)
api = Api(user_bp)

# user data
parser = reqparse.RequestParser()
parser.add_argument('username', type=str, help='Provide username')
parser.add_argument('email', type=str, help='Provide email')
parser.add_argument('password', type=str, help='Provide password')
parser.add_argument('confirm_password', type=str,
                    help='Provide confirm password')
parser.add_argument('full_name', type=str, help='Provide full name')


class Users(Resource):
    def get(self):
        users_lc = [user.to_dict() for user in User.query.all()]

        response = make_response(jsonify(users_lc), 200)

        return response

    def post(self):
        # access user data
        args = parser.parse_args()
        password = args("password")
        confirm_password = args("password")

        if not password == confirm_password:
            return {"error": "Passwords do not match!"}, 401

        new_user = User(
            username=args["username"],
            email=args["email"],
            _password_hash=bcrypt.generate_password_hash(
                password.encode('utf-8'))
        )

        db.session.add(new_user)
        db.session.commit()

        response = make_response(jsonify(new_user.to_dict()), 201)

        return response


class UserById(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id == user_id).first()

        if not user:
            return {"error": "User not found!"}, 404

        response = make_response(jsonify(user.to_dict()), 200)

        return response

    def patch(self, user_id):
        user = User.query.filter_by(id == user_id).first()

        args = parser.parse_args()

        for attr in args:
            setattr(user, attr, args.get(attr))

        db.session.commit()

        response = make_response(jsonify(user.to_dict()), 200)

        return response

    def delete(self, user_id):
        user = User.query.filter_by(id == user_id).first()

        # delete
        user_posts = Post.query.filter_by(user_id == user_id).all()
        user_comments = Comment.query.filter_by(user_id == user_id).all()
        user_votes = Post.query.filter_by(user_id == user_id).all()

        Post.query.delete(user_posts)
        Comment.query.delete(user_comments)
        Vote.query.delete(user_votes)

        return {"message": "User account deleted successfully"}, 200


api.add_resource(Users, "/users")
api.add_resource(UserById, "/users/<int:user_id>")
