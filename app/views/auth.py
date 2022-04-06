from flask import Blueprint, request, jsonify
from app.models.user import User

auth_views = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_views.route('/register', methods=['POST'])
def register():
    try:
        form_data = request.get_json()

        name = form_data['name']
        email = form_data['email']
        password = form_data['password']

        user = User(name, email, password)
        return user.register_user()

    except Exception as e:
        return {"exception": str(e)}, 403


@auth_views.route('/login', methods=['POST'])
def login():
    try:
        form_data = request.get_json()

        email = form_data['email']
        password = form_data['password']

        response = User.authenticate(email, password)

        if response is None:
            return {"error": "Invalid email or password"}, 401

        return jsonify(response)

    except Exception as e:
        return {"exception": str(e)}, 403
