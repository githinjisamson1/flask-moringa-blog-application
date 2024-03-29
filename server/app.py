from flask import request, jsonify, make_response
from flask_restful import Resource
import jwt
from server.config import app, api
from server.controllers.post_controllers import post_bp
from server.controllers.user_controllers import user_bp
from server.controllers.comment_controllers import comment_bp
from server.controllers.vote_controllers import vote_bp
from server.models import User
from server.auth_middleware import token_required

# register blueprints
app.register_blueprint(post_bp)
app.register_blueprint(user_bp)
app.register_blueprint(comment_bp)
app.register_blueprint(vote_bp)


# Define resources
class Index(Resource):
    def get(self):
        return {"message": "Welcome to Thee Moringa Blog API"}, 200


class Login(Resource):
    def post(self):
        try:
            data = request.get_json()

            if not data:
                return {
                    "message": "Please provide user details",
                    "data": None,
                    "error": "Bad request"
                }, 400

            # validate input
            username = data["username"]
            user = User.query.filter(User.username == username).first()
            if not user:
                return {
                    "message": "Please provide user details",
                    "data": None,
                    "error": "Username not found"
                }, 404

            password = data['password']
            if user.authenticate(password):
                try:
                    # generate token
                    # token should expire after 24 hrs
                    user.token = jwt.encode(
                        {"user_id": str(user.id)},
                        app.config["SECRET_KEY"],
                        algorithm="HS256"
                    )
                    # print(user.token)

                    return make_response(jsonify({
                        "message": "Successfully fetched auth token",
                        "data": user.to_dict(),
                        "auth_token": user.token
                    }), 200)

                except Exception as e:
                    return {
                        "error": "Something went wrong",
                        "message": str(e)
                    }, 500

            return {
                "message": "Error fetching auth token!, invalid username or password",
                "data": None,
                "error": "Unauthorized"
            }, 404
            
        except Exception as e:
            return {
                "message": "Something went wrong!",
                "error": str(e),
                "data": None
            }, 500


class Logout(Resource):
    @token_required
    def get(current_user, *args):
        current_user = None
        return {}, 200


# Add resources to the API
api.add_resource(Index, '/')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')

# Run the application
if __name__ == '__main__':
    app.run(port=5555, debug=True)
