from flask import Blueprint, request
from controllers.client.client_delete_controller import client_delete_controller
from flask_jwt_extended import jwt_required

client_delete_blueprint = Blueprint('client_delete_blueprint', __name__)

@client_delete_blueprint.route('/client/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_client(id):
    return client_delete_controller(id)
