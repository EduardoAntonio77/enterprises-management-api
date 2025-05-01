from flask import Blueprint, request, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required

from middlewares.client.client_create_middleware import client_create
from controllers.client.client_create_controller import client_create_controller

client_create_blueprint = Blueprint('create_client_blueprint', __name__)

@client_create_blueprint.route("/client", methods=['POST'])
@jwt_required()
@swag_from("../../../docs/client_docs/client_create_docs.yaml")
def register_client():

    data = request.json

    error = client_create(data)
    if error:
        return jsonify({
            'status': 400,
            'error': error
        }), 400

    client_create_controller(data)

    return jsonify({
        "status": 200,
        'message': 'Successfully registered client'
    })
