from flask import Blueprint, request, jsonify
from controllers.client.client_edit_controller import client_edit_controller
from middlewares.client.client_edit_middleware import client_edit_middleware

client_edit_blueprint = Blueprint('client_edit_blueprint', __name__)

@client_edit_blueprint.route('/client/<int:id>', methods=['PUT'])
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
        'message': 'Enterprise updated successfully'
    }), 200
