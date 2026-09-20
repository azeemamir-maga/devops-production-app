import os
import logging

from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv

from models import db

load_dotenv()


def create_app():
    app = Flask(__name__)

    # Application configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    # Logging configuration
    app.logger.setLevel(logging.INFO)
    app.logger.info("DevOps Production App started")

    # Database
    db.init_app(app)

    # Database migrations
    Migrate(app, db)

    # Routes
    from app.main import main
    app.register_blueprint(main)

    return app
