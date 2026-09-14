import os

from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv

from models import db

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    db.init_app(app)

    Migrate(app, db)

    from app.main import main
    app.register_blueprint(main)

    return app
