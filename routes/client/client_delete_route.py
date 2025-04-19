from flask import Blueprint, request
from controllers.client.client_delete_controller import client_delete_controller

client_delete_blueprint = Blueprint('client_delete_blueprint', __name__)

@client_delete_blueprint.route('/client/<int:id>', methods=['DELETE'])
def delete_client(id):
    return client_delete_controller(id)
