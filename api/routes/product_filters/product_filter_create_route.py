from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from middlewares.product_filters.product_filter_create_middleware import product_filters_create
from controllers.product_filters.product_filter_create_controller import create_filter

product_filter_create_blueprint = Blueprint('create_product_filter_blueprint', __name__)

@product_filter_create_blueprint.route("/product_filter", methods=['POST'])
@jwt_required()
def register_product():

    data = request.json

    error = product_filters_create(data)
    if error:
        return jsonify({
            'status': 400,
            'error': error
        }), 400
    
    create_filter(data)

    return jsonify({
        'status': 200,
        'message': 'Successfully registered product filter'
    })