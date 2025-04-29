from flask import Blueprint, request, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required

from middlewares.product.product_create_middleware import product_create
from controllers.product.product_create_controller import product_create_controller

product_create_blueprint = Blueprint('create_product_blueprint', __name__)

@product_create_blueprint.route("/product", methods=['POST'])
@jwt_required()
@swag_from({
    'tags': ['Product'],
    'description': 'Endpoint para registrar um novo produto.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'Cadeira de Escritório'},
                    'price': {'type': 'number', 'example': 299.99},
                    'stock': {'type': 'integer', 'example': 150}
                },
                'required': ['name', 'price', 'stock']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Produto registrado com sucesso.',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Successfully registered product'
                }
            }
        },
        400: {
            'description': 'Erro de validação dos dados enviados.',
            'examples': {
                'application/json': {
                    'status': 400,
                    'message': 'Campo "name" é obrigatório.'
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
def register_product():
    """
    Endpoint para criação de produtos.
    """
    data = request.json

    error = product_create(data)
    if error:
        return jsonify({
            'status': 400,
            'error': error
        }), 400

    product_create_controller(data)

    return jsonify({
        "status": 200,
        'message': 'Successfully registered product'
    })
