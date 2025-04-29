from flask import jsonify, Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from

# Importando middlewares e controllers
from middlewares.enterprise.enterprise_delete_middleware import enterprise_delete_middleware
from controllers.enterprise.enterprise_delete_controller import enterprise_delete_controller

# Criando blueprint para a rota
enterprise_delete_blueprint = Blueprint('enterprise_delete_route', __name__)

@enterprise_delete_blueprint.route('/enterprise/<int:id>', methods=['DELETE'])
@jwt_required()
@swag_from({
    'tags': ['Enterprise'],
    'description': 'Endpoint para excluir uma empresa pelo ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID da empresa a ser deletada',
            'example': 1
        }
    ],
    'responses': {
        200: {
            'description': 'Empresa excluída com sucesso.',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Representative successfully deleted!'
                }
            }
        },
        400: {
            'description': 'Erro ao tentar excluir a empresa, talvez o ID não exista.',
            'examples': {
                'application/json': {
                    'status': 400,
                    'message': 'Erro: Empresa não encontrada.'
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
def delete_enterprise(id):
    """
    Endpoint para excluir uma empresa pelo ID.
    """
    # Chama o middleware para validar a exclusão da empresa
    error = enterprise_delete_middleware(id)
    
    if error:
        return jsonify({
            'status': 400,
            'message': error
        }), 400

    # Chama o controller para efetuar a exclusão
    enterprise_delete_controller(id)
    
    return jsonify({
        'status': 200,
        'message': 'Representative successfully deleted!'  # Corrigir a mensagem, se necessário
    }), 200
