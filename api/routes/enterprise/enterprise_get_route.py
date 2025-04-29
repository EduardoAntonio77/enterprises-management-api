from flask import Blueprint, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from controllers.enterprise.enterprise_get_controller import get_enterprises

# Criando um blueprint para a rota
enterprise_get_blueprint = Blueprint('enterprise_get_route', __name__)

@enterprise_get_blueprint.route('/enterprise', methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['Enterprise'],
    'description': 'Endpoint para obter a lista de empresas.',
    'responses': {
        200: {
            'description': 'Lista de empresas recuperada com sucesso.',
            'examples': {
                'application/json': {
                    'status': 200,
                    'data': [
                        {
                            'id': 1,
                            'name': 'Empresa A',
                            'email': 'empresaA@example.com',
                            'address': 'Rua A, 123'
                        },
                        {
                            'id': 2,
                            'name': 'Empresa B',
                            'email': 'empresaB@example.com',
                            'address': 'Rua B, 456'
                        }
                    ]
                }
            }
        },
        401: {
            'description': 'Token de autenticação inválido ou ausente.',
            'examples': {
                'application/json': {
                    'status': 401,
                    'message': 'Token de autenticação ausente ou inválido.'
                }
            }
        }
    }
})
def enterprise_get():
    """
    Endpoint para obter a lista de empresas.
    """
    return jsonify(get_enterprises()), 200
