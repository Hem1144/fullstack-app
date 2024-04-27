from flask import Blueprint

api = Blueprint("/api", __name__)


@api.route("/posts", methods=["GET"])
def get_posts():
    return {"status": "OK"}


@api.route("/posts/<int:id>", methods=["GET"])
def get_post(id):
    pass


@api.route("/posts", methods=["POST"])
def create_post():
    pass


@api.route("/posts/<int:id>", methods=["PUT"])
def update_post(id):
    pass


@api.route("/posts/<int:id>", methods=["DELETE"])
def delete_post(id):
    pass


# Similar routes for categories, tags, and comments
