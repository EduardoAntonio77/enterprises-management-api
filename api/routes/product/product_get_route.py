from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from controllers.product.product_get_controller import get_products

product_get_blueprint = Blueprint('product_get_route', __name__)

@product_get_blueprint.route("/product", methods=["GET"])
@jwt_required()
@swag_from({
    'tags': ['Product'],
    'description': 'Endpoint para obter uma lista de todos os produtos.',
    'responses': {
        200: {
            'description': 'Lista de produtos retornada com sucesso.',
            'examples': {
                'application/json': {
                    'status': 200,
                    'data': [
                        {
                            'id': 1,
                            'name': 'Produto A',
                            'price': 99.99,
                            'description': 'Descrição do Produto A'
                        },
                        {
                            'id': 2,
                            'name': 'Produto B',
                            'price': 150.75,
                            'description': 'Descrição do Produto B'
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
def product_get():
    """
    Endpoint para obter uma lista de todos os produtos.
    """
    return jsonify(get_products()), 200
