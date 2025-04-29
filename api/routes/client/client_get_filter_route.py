from flask import Blueprint, g
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from controllers.client.client_get_filter_controller import client_filter
from middlewares.client.client_get_filter_middleware import client_search

client_get_filter_blueprint = Blueprint('client_get_filter_route', __name__)

@client_get_filter_blueprint.route("/client/<int:id>", methods=['GET'])
@client_search
@jwt_required()
@swag_from({
    'tags': ['Client'],
    'description': 'Endpoint para buscar um cliente específico pelo seu ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do cliente a ser buscado.',
            'example': 1
        }
    ],
    'responses': {
        200: {
            'description': 'Cliente encontrado com sucesso!',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Client found',
                    'data': {
                        'id': 1,
                        'name': 'Cliente Exemplo',
                        'email': 'cliente@exemplo.com',
                        'phone': '+55 11 91234-5678'
                    }
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
def client_get_filter(id, client):
    """
    Endpoint paa buscar um cliente específico
    """
    return client_filter(
        client=client, id=id
    )
