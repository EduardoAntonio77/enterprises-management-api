from flask import Blueprint, request
from flasgger import swag_from
from flask_jwt_extended import jwt_required

# Importando o controller
from controllers.client.client_delete_controller import client_delete_controller

client_delete_blueprint = Blueprint('client_delete_blueprint', __name__)

@client_delete_blueprint.route('/client/<int:id>', methods=['DELETE'])
@jwt_required()
@swag_from({
    'tags': ['Client'],
    'description': 'Endpoint para deletar um cliente.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do cliente que será deletado.',
            'example': 1
        }
    ],
    'responses': {
        200: {
            'description': 'Cliente deletado com sucesso!',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Client successfully deleted'
                }
            }
        },
        404: {
            'description': 'Cliente não encontrado.',
            'examples': {
                'application/json': {
                    'status': 404,
                    'message': 'Client not found'
                }
            }
        },
        401: {
            'description': 'Token JWT inválido ou não fornecido.',
            'examples': {
                'application/json': {
                    'status': 401,
                    'message': 'Token is missing or invalid'
                }
            }
        }
    }
})
def delete_client(id):
    """
    Endpoint para deletar um cliente
    """
    return client_delete_controller(id)
