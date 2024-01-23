from server.config import app, api
from flask import make_response, jsonify
from flask_restful import Resource
from server.controllers.user_controllers import user_bp

app.register_blueprint(user_bp)


# !RESOURCES
class Index(Resource):
    # !GET
    def get(self):
        response = make_response(jsonify({
            "success": True,
            "message": "Welcome to Thee Moringa Blog!"
        }), 200)

        response.headers["Content-Type"] = "application/json"

        return response


# !ROUTES
api.add_resource(Index, "/")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
