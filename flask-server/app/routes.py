# app/routes.py

from flask import Blueprint, jsonify, request
# from app import db  

api = Blueprint("api", __name__)

posts = []
categories = []
tags = []


def validate_post(post):
    required_fields = ["title", "content", "author", "category", "tags"]
    if not all(field in post for field in required_fields):
        return False
    return True


def validate_category(category):
    if "name" not in category:
        return False
    return True


def validate_tag(tag):
    if "name" not in tag:
        return False
    return True


# Routes for CRUD operations on posts
@api.route("/posts", methods=["GET"])
def get_posts():
    return jsonify(posts)


@api.route("/posts", methods=["POST"])
def create_post():
    data = request.json
    if validate_post(data):
        posts.append(data)
        return jsonify({"message": "Post created successfully"}), 201
    else:
        return jsonify({"error": "Invalid post data"}), 400


@api.route("/posts/<int:id>", methods=["GET"])
def get_post(id):
    if id < len(posts):
        return jsonify(posts[id])
    else:
        return jsonify({"error": "Post not found"}), 404


@api.route("/posts/<int:id>", methods=["PUT"])
def update_post(id):
    if id < len(posts):
        data = request.json
        if validate_post(data):
            posts[id] = data
            return jsonify({"message": "Post updated successfully"}), 200
        else:
            return jsonify({"error": "Invalid post data"}), 400
    else:
        return jsonify({"error": "Post not found"}), 404


@api.route("/posts/<int:id>", methods=["DELETE"])
def delete_post(id):
    if id < len(posts):
        del posts[id]
        return jsonify({"message": "Post deleted successfully"}), 200
    else:
        return jsonify({"error": "Post not found"}), 404


# Routes for CRUD operations on categories
@api.route("/categories", methods=["GET"])
def get_categories():
    return jsonify(categories)


@api.route("/categories", methods=["POST"])
def create_category():
    data = request.json
    if validate_category(data):
        categories.append(data)  # Append to categories list
        return jsonify({"message": "Category created successfully"}), 201
    else:
        return jsonify({"error": "Invalid category data"}), 400


# Routes for CRUD operations on tags
@api.route("/tags", methods=["GET"])
def get_tags():
    return jsonify(tags)


@api.route("/tags", methods=["POST"])
def create_tag():
    data = request.json
    if validate_tag(data):
        tags.append(data)  # Append to tags list
        return jsonify({"message": "Tag created successfully"}), 201
    else:
        return jsonify({"error": "Invalid tag data"}), 400
