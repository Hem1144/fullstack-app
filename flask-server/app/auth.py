from flask import Blueprint

auth = Blueprint("/auth", __name__)


@auth.route("/login", methods=["POST"])
def login():
    pass


@auth.route("/logout", methods=["POST"])
def logout():
    pass
