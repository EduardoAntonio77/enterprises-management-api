from flask import Blueprint, request, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required

# Importando middlewares e controllers
from middlewares.client.client_create_middleware import client_create
from controllers.client.client_create_controller import client_create_controller

# Criando blueprint para registrar a rota
client_create_blueprint = Blueprint('create_client_blueprint', __name__)

@client_create_blueprint.route("/client", methods=['POST'])
@jwt_required()
@swag_from({
    'tags': ['Client'],
    'description': 'Endpoint para registrar um novo cliente.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'João da Silva'},
                    'email': {'type': 'string', 'example': 'joao.silva@empresa.com'},
                    'phone': {'type': 'string', 'example': '+55 11 91234-5678'}
                },
                'required': ['name', 'email', 'phone']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Cliente registrado com sucesso!',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Successfully registered client'
                }
            }
        },
        400: {
            'description': 'Erro na validação dos dados enviados.',
            'examples': {
                'application/json': {
                    'status': 400,
                    'message': 'Erro: nome do cliente é obrigatório.'
                }
            }
        }
    }
})
def register_client():
    """
    Endpoint para criação de clientes
    """
    # Criando uma variavel que irá receber os dados que o usuário passou na rota usando o método POST.
    data = request.json

    # Validando os dados com o middleware
    error = client_create(data)
    if error:
        return jsonify({
            'status': 400,
            'error': error
        }), 400

    # Usando o controller para criar o cliente
    client_create_controller(data)

    return jsonify({
        "status": 200,
        'message': 'Successfully registered client'
    })
