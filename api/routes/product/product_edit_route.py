from flask import Blueprint, request, jsonify
from flasgger import swag_from
from middlewares.product.product_edit_middleware import product_edit
from controllers.product.product_edit_controller import product_edit_controller
from flask_jwt_extended import jwt_required

product_edit_blueprint = Blueprint('product_edit_blueprint', __name__)

@product_edit_blueprint.route("/product/<int:id>", methods=['PUT'])
@jwt_required()
@swag_from({
    'tags': ['Product'],
    'description': 'Endpoint para editar um produto pelo ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do produto a ser editado',
            'example': 1
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'Produto Editado'},
                    'price': {'type': 'number', 'format': 'float', 'example': 99.99},
                    'description': {'type': 'string', 'example': 'Descrição do produto editada'}
                },
                'required': ['name', 'price']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Produto atualizado com sucesso.',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Product updated successfully'
                }
            }
        },
        400: {
            'description': 'Erro na validação dos dados ou erro no controller.',
            'examples': {
                'application/json': {
                    'status': 400,
                    'error': 'Erro: O nome do produto é obrigatório.'
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
def edit_product(id):
    """
    Endpoint para editar um produto pelo ID.
    """
    data = request.json

    # Validando os dados do produto
    error = product_edit(data, id)
    if error:
        return jsonify({
            'status': 400,
            'error': error
        }), 400

    # Editando o produto no controller
    controller_error = product_edit_controller(id, data)
    if controller_error:
        return jsonify({
            'status': 400,
            'error': controller_error
        }), 400

    return jsonify({
        'status': 200,
        'message': 'Product updated successfully'
    })
