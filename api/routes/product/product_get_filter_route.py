from flask import Blueprint, g
from flasgger import swag_from
from middlewares.product.product_get_filter_middleware import product_search
from controllers.product.product_get_filter_controller import product_filter
from flask_jwt_extended import jwt_required

product_get_filter_blueprint = Blueprint("product_get_filter_route", __name__)

@product_get_filter_blueprint.route("/product/<int:id>", methods=["GET"])
@product_search
@jwt_required()
@swag_from({
    'tags': ['Product'],
    'description': 'Endpoint para obter os detalhes de um produto pelo ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do produto a ser consultado',
            'example': 1
        }
    ],
    'responses': {
        200: {
            'description': 'Produto encontrado com sucesso.',
            'examples': {
                'application/json': {
                    'status': 200,
                    'data': {
                        'id': 1,
                        'name': 'Produto A',
                        'price': 99.99,
                        'description': 'Descrição do Produto A'
                    }
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
        },
        404: {
            'description': 'Produto não encontrado.',
            'examples': {
                'application/json': {
                    'status': 404,
                    'error': 'Produto não encontrado'
                }
            }
        }
    }
})
def product_get(id, product):
    """
    Endpoint para obter os detalhes de um produto pelo ID.
    """
    return product_filter(product=product, id=id)
