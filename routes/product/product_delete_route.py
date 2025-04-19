from flask import Blueprint, jsonify

from middlewares.product.product_delete_middleware import product_delete
from controllers.product.product_delete_controller import product_delete_controller

product_delete_blueprint = Blueprint('delete_product_blueprint', __name__)

@product_delete_blueprint.route("/product/<int:id>", methods=['DELETE'])
def delete_product(id):
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
