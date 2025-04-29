from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flasgger import swag_from

# Importando middlewares e controllers
from middlewares.enterprise.enterprise_create_middleware import enterprise_create
from controllers.enterprise.enterprise_create_controller import create_enterprise

# Criando um blueprint para registrar a rota em app.py
create_enterprise_blueprint = Blueprint('create_enterprise_blueprint', __name__)

@create_enterprise_blueprint.route('/enterprise', methods=['POST'])
@jwt_required()
@swag_from({
    'tags': ['Enterprise'],
    'description': 'Endpoint para registrar uma nova empresa.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'Tech Solutions'},
                    'address': {'type': 'string', 'example': 'Rua das Empresas, 123'},
                    'email': {'type': 'string', 'example': 'contato@techsolutions.com.br'},
                    'phone': {'type': 'string', 'example': '+55 11 91234-5678'}
                },
                'required': ['name', 'address', 'email', 'phone']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Empresa registrada com sucesso.',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Successfully registered enterprise'
                }
            }
        },
        400: {
            'description': 'Erro na validação dos dados enviados.',
            'examples': {
                'application/json': {
                    'status': 400,
                    'error': 'Campo "name" é obrigatório.'
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
def register_enterprise():
    """
    Endpoint para registrar uma nova empresa.
    """
    # Dados recebidos via POST
    data = request.json

    # Validando os dados com middleware
    error = enterprise_create(data)
    if error:
        return jsonify({
            'status': 400,
            'error': error
        }), 400

    # Criando a empresa através do controller
    create_enterprise(data)

    return jsonify({
        'status': 200,
        'message': "Successfully registered enterprise"
    })
