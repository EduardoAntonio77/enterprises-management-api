from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from controllers.client.client_get_controller import get_clients

client_get_blueprint = Blueprint('client_get_route', __name__)

@client_get_blueprint.route("/client", methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['Client'],
    'description': 'Endpoint para listar todos os clientes registrados.',
    'responses': {
        200: {
            'description': 'Lista de clientes retornada com sucesso!',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Clients found',
                    'data': [
                        {
                            'id': 1,
                            'name': 'Cliente 1',
                            'email': 'cliente1@exemplo.com',
                            'phone': '+55 11 91234-5678'
                        },
                        {
                            'id': 2,
                            'name': 'Cliente 2',
                            'email': 'cliente2@exemplo.com',
                            'phone': '+55 11 98765-4321'
                        }
                    ]
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
def client_get():
    """
    Endpoint para listar todos os clientes
    """
    return jsonify(get_clients()), 200
