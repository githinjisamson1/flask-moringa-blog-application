from os import environ
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from dotenv import load_dotenv

# Invoke load_dotenv to load environment variables
load_dotenv()

# instantiate Flask app
app = Flask(__name__)

# Define metadata with a specific naming convention
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# Instantiate SQLAlchemy with the provided metadata
db = SQLAlchemy(metadata=metadata)

# Define the absolute path for the SQLite database
db_path = "/home/samson_githinji/Moringa-Development/code/phase-4/moringa-blog-application/server/instance/moringa.db"

# configure Flask with SQLAlchemy settings
app.secret_key = environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

# prevent cross origin isssues
CORS(app)

# Instantiate Flask-Migrate extension
migrate = Migrate(app, db)

# Initialize SQLAlchemy extension with the Flask app
db.init_app(app)

# Instantiate Bcrypt extension with the Flask app
bcrypt = Bcrypt(app)

# Instantiate Flask-RESTful Api with the Flask app
api = Api(app)
