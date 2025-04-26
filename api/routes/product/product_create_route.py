from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from middlewares.product.product_create_middleware import product_create
from controllers.product.product_create_controller import product_create_controller

product_create_blueprint = Blueprint('create_product_blueprint', __name__)
@product_create_blueprint.route("/product", methods=['POST'])
@jwt_required()
def register_product():
    data = request.json;

    error = product_create(data)
    if error:
        return jsonify({
            'status': 400,
            'error': error
        }), 400;

    product_create_controller(data)

    return jsonify({
        "status": 200,
        'message': 'Successfully registered product'
    })