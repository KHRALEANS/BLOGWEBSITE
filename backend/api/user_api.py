import inject
from flask import request, jsonify
from backend.models.user_model import User
from backend.services.user_service import UserService
from backend.api import bp

user_service = inject.instance(UserService)

@bp.route('/user/create/', methods=['POST'])
def create_user():
    email = request.json['email']
    password = request.json['password']
    first_name = request.json['first_name']

    user = User(email=email, password=password, first_name=first_name)
    user_service.add(user)

    return jsonify(user.to_json())
