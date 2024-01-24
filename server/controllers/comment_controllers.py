from flask import Blueprint, make_response, jsonify, request
from flask_restful import Api, Resource, reqparse
from server.models import Comment
from server.config import db

# instantiations
comment_bp = Blueprint("comment_bp", __name__)
api = Api(comment_bp)

# comment data
parser = reqparse.RequestParser()
parser.add_argument('content', type=str, help='Provide content')
parser.add_argument('user_id', type=int, help='Provide user id')
parser.add_argument('post_id', type=int, help='Provide post id')


# resources
class Comments(Resource):
    def get(self):

        comment_lc = [comment.to_dict() for comment in Comment.query.all()]

        response = make_response(jsonify(comment_lc), 200)

        return response

    def post(self):
        try:
            # access comment data
            args = parser.parse_args()

            # create new comment
            new_comment = Comment(
                content=args["content"],
                user_id=args["user_id"],
                comment_id=args["comment_id"]

            )
            # add to db
            db.session.add(new_comment)
            db.session.commit()

            response = make_response(jsonify(new_comment.to_dict()), 201)

            return response

        except ValueError as e:
            return {"error": [str(e)]}, 401


class CommentByID(Resource):
    def get(self, comment_id):
        comment = Comment.query.filter_by(id=comment_id).first()

        if not comment:
            return {"error": "Comment not found!"}, 404

        response = make_response(jsonify(comment.to_dict()), 201)

        return response

    def patch(self, comment_id):
        try:
            data = request.get_json()

            comment = Comment.query.filter_by(id=comment_id).first()

            for attr in data:
                setattr(comment, attr, data.get(attr))

            db.session.commit()

            return make_response(jsonify(comment.to_dict()), 200)

        except ValueError as e:
            return {"error": [str(e)]}

    def delete(self, comment_id):
        comment = Comment.query.filter_by(id=comment_id).first()

        if not comment:
            return {"error": "Comment not found!"}, 404

        db.session.delete(comment)

        db.session.commit()

        response_body = {
            "message": "Comment deleted successfully"
        }
        response = make_response(jsonify(response_body), 200)

        return response


api.add_resource(Comments, "/comments")
api.add_resource(CommentByID, "/comments/<int:comment_id>")
