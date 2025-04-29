from flask import Blueprint, request, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required

# Importando os middlewares e controllers
from controllers.client.client_edit_controller import client_edit_controller
from middlewares.client.client_edit_middleware import client_edit_middleware

client_edit_blueprint = Blueprint('client_edit_blueprint', __name__)

@client_edit_blueprint.route('/client/<int:id>', methods=['PUT'])
@jwt_required()
@swag_from({
    'tags': ['Client'],
    'description': 'Endpoint para editar as informações de um cliente.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do cliente a ser atualizado.',
            'example': 1
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'Nome do Cliente'},
                    'email': {'type': 'string', 'example': 'email@cliente.com'},
                    'phone': {'type': 'string', 'example': '+55 11 91234-5678'}
                },
                'required': ['name', 'email', 'phone']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Cliente atualizado com sucesso!',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Enterprise updated successfully'
                }
            }
        },
        404: {
            'description': 'Cliente não encontrado.',
            'examples': {
                'application/json': {
                    'status': 404,
                    'message': 'Enterprise not found'
                }
            }
        },
        400: {
            'description': 'Erro ao tentar atualizar o cliente.',
            'examples': {
                'application/json': {
                    'status': 400,
                    'message': 'Error updating client'
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
def client_edit(id):
    """
    Endpoint para editar as informações de um cliente
    """
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
