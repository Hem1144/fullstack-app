from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os


def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    db = SQLAlchemy(app)

    from app.routes import api
    from app.auth import auth

    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(auth, url_prefix="/auth")

    print("Database connected successfully.")

    return app, db
