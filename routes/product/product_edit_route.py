from flask import Blueprint, request, jsonify
from middlewares.product.product_edit_middleware import product_edit
from controllers.product.product_edit_controller import product_edit_controller

product_edit_blueprint = Blueprint('product_edit_blueprint', __name__)

@product_edit_blueprint.route("/product/<int:id>", methods=['PUT'])
def edit_product(id):
    data = request.json

    error = product_edit(data, id)
    if error:
        return jsonify({
            'status': 400,
            'error': error
        }), 400

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
