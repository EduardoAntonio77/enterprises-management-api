from flask import Blueprint, request
from flasgger import swag_from
from flask_jwt_extended import jwt_required

from controllers.client.client_delete_controller import client_delete_controller

client_delete_blueprint = Blueprint('client_delete_blueprint', __name__)

@client_delete_blueprint.route('/client/<int:id>', methods=['DELETE'])
@jwt_required()
@swag_from("../../../docs/client_docs/client_delete_docs.yaml")
def delete_client(id):

    return client_delete_controller(id)
