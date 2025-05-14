from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from middlewares.product_filters.product_filter_delete_middleware import product_filter_delete_midlleware
from controllers.product_filters.product_filter_delete_controller import product_filter_delete_controller

product_filter_delete_blueprint = Blueprint('delete_product_filter_blueprint', __name__)

@product_filter_delete_blueprint.route("/product_filter/<int:filter_id>", methods=['DELETE'])
@jwt_required()
def delete_product_filter(filter_id):

    error = product_filter_delete_midlleware(filter_id)
    if error:
        return jsonify({
            'status': 404,
            'error': error
        }), 404
    
    product_filter_delete_controller(filter_id)

    return jsonify({
        "status": 200,
        "message": "Product filter successfully deleted"
    })