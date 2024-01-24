from flask import Blueprint, make_response, jsonify, request
from flask_restful import Api, Resource, reqparse
from server.models import Vote
from server.config import db

# instantiations
vote_bp = Blueprint("vote_bp", __name__)
api = Api(vote_bp)

# vote data
parser = reqparse.RequestParser()
parser.add_argument('vote_type', type=str, help='Provide vote type')



# resources
class Votes(Resource):

    def get(self):

        votes_lc = [vote.to_dict() for vote in Vote.query.all()]

        response = make_response(jsonify(votes_lc), 200)

        return response

    def post(self):
        try:
            # access vote data
            args = parser.parse_args()

            # create new vote
            new_vote = Vote(
                vote_type=args["vote_type"],
                
            )
            # add to db
            db.session.add(new_vote)
            db.session.commit()

            response = make_response(jsonify(new_vote.to_dict()), 201)

            return response

        except ValueError as e:
            return {"error": [str(e)]}, 401


class VoteByID(Resource):
    def get(self, vote_id):
        vote = Vote.query.filter_by(id=vote_id).first()

        if not vote:
            return {"error": "Vote not found!"}, 404

        response = make_response(jsonify(vote.to_dict()), 201)

        return response

    def patch(self, vote_id):
        try:
            data = request.get_json()

            vote = Vote.query.filter_by(id=vote_id).first()

            for attr in data:
                setattr(vote, attr, data.get(attr))

            db.session.commit()

            return make_response(jsonify(vote.to_dict()), 200)

        except ValueError as e:
            return {"error": [str(e)]}

    def delete(self, vote_id):
        vote = Vote.query.filter_by(id=vote_id).first()

        if not vote:
            return {"error": "Vote not found!"}, 404

        db.session.delete(vote)

        db.session.commit()

        response_body = {
            "message": "Vote deleted successfully"
        }
        response = make_response(jsonify(response_body), 200)

        return response


api.add_resource(Votes, "/votes")
api.add_resource(VoteByID, "/votes/<int:vote_id>")
