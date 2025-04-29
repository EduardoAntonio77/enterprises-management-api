from flask import Blueprint, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required

from middlewares.product.product_delete_middleware import product_delete
from controllers.product.product_delete_controller import product_delete_controller

product_delete_blueprint = Blueprint('delete_product_blueprint', __name__)

@product_delete_blueprint.route("/product/<int:id>", methods=['DELETE'])
@jwt_required()
@swag_from({
    'tags': ['Product'],
    'description': 'Endpoint para deletar um produto pelo ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do produto a ser deletado',
            'example': 1
        }
    ],
    'responses': {
        200: {
            'description': 'Produto deletado com sucesso.',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Product successfully deleted'
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
def delete_product(id):
    """
    Endpoint para deletar um produto pelo ID.
    """

    error = product_delete(id)
    if error:
        return jsonify({
            'status': 404,
            'error': error
        }), 404

    product_delete_controller(id)

    return jsonify({
        "status": 200,
        "message": "Product successfully deleted"
    })
