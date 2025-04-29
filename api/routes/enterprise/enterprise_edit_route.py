from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from

# Importando middlewares e controllers
from middlewares.enterprise.enterprise_edit_middleware import enterprise_edit_middleware
from controllers.enterprise.enterprise_edit_controller import enterprise_edit_controller

# Criando blueprint para a rota
enterprise_edit_blueprint = Blueprint('enterprise_edit_route', __name__)

@enterprise_edit_blueprint.route("/enterprise/<int:id>", methods=['PUT'])
@jwt_required()
@swag_from({
    'tags': ['Enterprise'],
    'description': 'Endpoint para editar uma empresa pelo ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID da empresa a ser editada',
            'example': 1
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'Empresa X'},
                    'email': {'type': 'string', 'example': 'empresa@example.com'},
                    'address': {'type': 'string', 'example': 'Rua Exemplo, 123'}
                },
                'required': ['name', 'email']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Empresa atualizada com sucesso.',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Enterprise updated successfully'
                }
            }
        },
        400: {
            'description': 'Erro de validação ou dados inválidos.',
            'examples': {
                'application/json': {
                    'status': 400,
                    'message': 'Erro: Dados de empresa inválidos.'
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
def edit_enterprise(id):
    """
    Endpoint para editar uma empresa pelo ID.
    """
    # Middleware para verificar se a empresa existe
    enterprise = enterprise_edit_middleware(id)
    if not enterprise:
        return jsonify({
            'status': 404,
            'error': 'Enterprise not found'
        }), 404
    
    # Recebendo os dados do corpo da requisição
    data = request.get_json()

    # Chamando o controller para atualizar os dados
