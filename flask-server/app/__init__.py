from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import api
from app.auth import auth

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SECRET_KEY"] = "dulalfullstack"
db = SQLAlchemy(app)

app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(auth, url_prefix="/auth")

if __name__ == "__main__":
    app.run(debug=True)
