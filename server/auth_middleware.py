from functools import wraps
import jwt
from flask import request, abort
from flask import current_app
from server.models import User


# Define token_required decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Extract the Authorization token from the request headers
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        # If token is missing, return Unauthorized response
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401

        try:
            # Decode the token using the app's secret key and HS256 algorithm
            data = jwt.decode(
                token, current_app.config['SECRET_KEY'], algorithms=['HS256'])

            # Retrieve the user associated with the decoded user_id from the token
            current_user = User.query.filter_by(id=data["user_id"]).first()

            # If user is not found, return Unauthorized response
            if current_user is None:
                return {
                    "message": "Invalid Authentication token!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401

            # Call the original function with the current_user and any additional arguments
            return f(current_user, *args, **kwargs)

        except Exception as e:
            # Return a 500 Internal Server Error response for any exception during token decoding
            return {
                "message": "Something went wrong here",
                "data": None,
                "error": str(e)
            }, 500

    return decorated
