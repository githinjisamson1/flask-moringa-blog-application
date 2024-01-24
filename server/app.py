from flask import make_response, jsonify
from flask_restful import Resource
from server.config import app, api
from server.controllers.user_controllers import user_bp
from server.controllers.post_controllers import post_bp
from server.controllers.comment_controllers import comment_bp
from server.controllers.vote_controllers import vote_bp

# !register blueprints
app.register_blueprint(user_bp)
app.register_blueprint(post_bp)
app.register_blueprint(comment_bp)
app.register_blueprint(vote_bp)


# resources
class Index(Resource):
    def get(self):
        return {
            "success": True,
            "message": "Welcome to Thee Moringa Blog!"
        }, 200


# resource + route
api.add_resource(Index, "/")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
