from flask import Blueprint, jsonify

common_views = Blueprint("common", __name__, url_prefix="")


@common_views.route('/', methods=['GET'])
def index():
    return jsonify({"data": "hello, world!"})
