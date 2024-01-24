from flask import Blueprint, make_response, jsonify, request
from flask_restful import Api, Resource, reqparse
from server.models import User, Post, Comment, Vote
from server.config import bcrypt, db

# instantiate Blueprint
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


# resources
class Users(Resource):
    def get(self):
        users_lc = [user.to_dict() for user in User.query.all()]

        response = make_response(jsonify(users_lc), 200)

        return response

    def post(self):
        try:
            # access user data/similar to request.get_json()
            args = parser.parse_args()

            password = args["password"]
            confirm_password = args["confirm_password"]

            if not password == confirm_password:
                return {"error": "Passwords do not match!"}, 401

            # proceed to create new_user
            new_user = User(
                username=args["username"],
                full_name=args["full_name"],
                email=args["email"],
                _password_hash=bcrypt.generate_password_hash(
                    password.encode('utf-8'))
            )

            db.session.add(new_user)
            db.session.commit()

            response = make_response(jsonify(new_user.to_dict()), 201)

            return response

        except ValueError as e:
            return {"error": [str(e)]}, 401


class UserById(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()

        if not user:
            return {"error": "User not found!"}, 404

        response = make_response(jsonify(user.to_dict()), 200)

        return response

    def patch(self, user_id):
        try:
            data = request.get_json()

            user = User.query.filter_by(id=user_id).first()

            for attr in data:
                setattr(user, attr, data.get(attr))

            db.session.commit()

            response = make_response(jsonify(user.to_dict()), 200)

            return response

        except ValueError as e:
            return {"error": [str(e)]}

    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()

        if not user:
            return {"error": "User not found!"}, 404

        user_posts = Post.query.filter_by(user_id=user_id).all()
        user_comments = Comment.query.filter_by(user_id=user_id).all()
        user_votes = Post.query.filter_by(user_id=user_id).all()

        # !delete user plus associated posts, comments, votes
        db.session.delete(user)

        if user_posts:
            Post.query.delete(user_posts)

        if user_comments:
            Comment.query.delete(user_comments)

        if user_votes:
            Vote.query.delete(user_votes)

        db.session.commit()

        return {"message": "User account deleted successfully"}, 200


# resources + routes
api.add_resource(Users, "/users")
api.add_resource(UserById, "/users/<int:user_id>")
