from flask import Blueprint, request, jsonify
from flasgger import swag_from
from middlewares.product.product_edit_middleware import product_edit
from controllers.product.product_edit_controller import product_edit_controller
from flask_jwt_extended import jwt_required

product_edit_blueprint = Blueprint('product_edit_blueprint', __name__)

@product_edit_blueprint.route("/product/<int:id>", methods=['PUT'])
@jwt_required()
@swag_from("../../../docs/product_docs/product_edit_docs.yaml")
def edit_product(id):

    data = request.json

    product = product_edit(data, id)
    if isinstance(product, str):
        return jsonify({
            'status': 404,
            'error': product
        }), 404

    
    error = product_edit_controller(product, data)
    if error:
        return jsonify({
            'status': 400,
            'error': error
        }), 400

    return jsonify({
        'status': 200,
        'message': 'Product updated successfully'
    }), 200
