from flask import request, jsonify, g
from config.jwt_utils.auth import authenticate_user

def login_required(func):
    def wrapper(*args, **kwargs):
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({
                'status': 400,
                'error': 'Email and password are required'
            }), 400

        rep = authenticate_user(email, password)

        if not rep:
            return jsonify({
                'status': 401,
                'error': 'Invalid login'
            }), 401

        g.representative = rep
        return func(*args, **kwargs)

    return wrapper
