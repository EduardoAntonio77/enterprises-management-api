from flask import Blueprint, request, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required

# Importando os middlewares e controllers
from controllers.client.client_edit_controller import client_edit_controller
from middlewares.client.client_edit_middleware import client_edit_middleware

client_edit_blueprint = Blueprint('client_edit_blueprint', __name__)

@client_edit_blueprint.route('/client/<int:id>', methods=['PUT'])
@jwt_required()
@swag_from("../../../docs/client_docs/client_edit_docs.yaml")
def client_edit(id):

    client = client_edit_middleware(id)
    if not client:
        return jsonify({
            'status': 404,
            'error': 'Enterprise not found'
        }), 404
    
    data = request.get_json()
    client_edit_controller(data, client)

    return jsonify({
        'status': 200,
        'message': 'Client updated successfully'
    }), 200
