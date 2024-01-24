from os import environ
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from dotenv import load_dotenv

# invoke load_dotenv
load_dotenv()

# instantiate Flask app
app = Flask(__name__)

# metadata
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# instatiate SQLAlchemy
db = SQLAlchemy(metadata=metadata)

# declare absolute path where to create instance/moringa.db
db_path = "/home/samson_githinji/Moringa-Development/code/phase-4/moringa-blog-application/server/instance/moringa.db"

# configure Flask with SQLAlchemy settings
app.secret_key = environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

# prevent cross origin isssues
CORS(app)

# instantiations
migrate = Migrate(app, db)
db.init_app(app)
bcrypt = Bcrypt(app)
api = Api(app)
