from flask import Blueprint, g
from flasgger import swag_from
from middlewares.enterprise.enterprise_get_filter_middleware import enterprise_search
from flask_jwt_extended import jwt_required
from controllers.enterprise.enterprise_get_filter_controller import enterprise_filter

# Criando um blueprint para a rota
enterprise_get_filter_blueprint = Blueprint('enterprise_get_filter_route', __name__)

@enterprise_get_filter_blueprint.route('/enterprise/<int:id>', methods=['GET'])
@enterprise_search
@jwt_required()
@swag_from({
    'tags': ['Enterprise'],
    'description': 'Endpoint para obter os dados de uma empresa pelo ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID da empresa que será filtrada',
            'example': 1
        }
    ],
    'responses': {
        200: {
            'description': 'Empresa encontrada com sucesso.',
            'examples': {
                'application/json': {
                    'status': 200,
                    'data': {
                        'id': 1,
                        'name': 'Empresa X',
                        'email': 'empresa@example.com',
                        'address': 'Rua Exemplo, 123'
                    }
                }
            }
        },
        404: {
            'description': 'Empresa não encontrada.',
            'examples': {
                'application/json': {
                    'status': 404,
                    'message': 'Enterprise not found'
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
def enterprise_get_filter(id, enterprise):
    """
    Endpoint para obter os dados de uma empresa pelo ID.
    """
    return enterprise_filter(enterprise=enterprise, id=id)
