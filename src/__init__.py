from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Init db
db = SQLAlchemy()


def create_app():
    # Load env variables
    load_dotenv()

    # Create app
    app = Flask(__name__)
    # Handling CORS
    CORS(app)

    # Config section
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}".format(
            DB_USER=os.getenv("DB_USER"),
            DB_PASSWORD=os.getenv("DB_PASSWORD"),
            DB_HOST=os.getenv("DB_HOST"),
            DB_NAME=os.getenv("DB_NAME"),
        )
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Connect the db to app
    db.init_app(app)

    # Init migration
    migrate = Migrate(app, db)

    # Import routes
    from src.routes.dummy_routes import dummy_bp
    app.register_blueprint(dummy_bp)

    return app
