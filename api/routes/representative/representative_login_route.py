from flask import Blueprint, jsonify, g
from flasgger import swag_from
from middlewares.representative.representative_login_middleware import login_required
from controllers.representative.representative_login_controller import representative_login

login_route = Blueprint("representative_login_route", __name__)

@login_route.route("/login", methods=["POST"])
@login_required
@swag_from({
    'tags': ['Representative'],
    'description': 'Endpoint para login de representantes.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {
                        'type': 'string',
                        'description': 'Email do representante.',
                        'example': 'joao.silva@email.com'
                    },
                    'password': {
                        'type': 'string',
                        'description': 'Senha do representante.',
                        'example': 'senha123'
                    }
                },
                'required': ['email', 'password']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Login realizado com sucesso!',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Login bem-sucedido!',
                    'token': 'jwt_token_aqui'  # Aqui é um exemplo de como a resposta pode incluir um token JWT
                }
            }
        },
        400: {
            'description': 'Erro na validação dos dados de login.',
            'examples': {
                'application/json': {
                    'status': 400,
                    'message': 'Erro: email ou senha inválidos.'
                }
            }
        }
    }
})
def login():
    """
    Endpoint para login de representantes.
    """
    login = representative_login()

    return jsonify(login), 200
