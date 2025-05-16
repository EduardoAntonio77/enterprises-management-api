from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from flasgger.utils import swag_from

from middlewares.product_filters.product_filter_create_middleware import product_filters_create
from controllers.product_filters.product_filter_create_controller import create_filter

product_filter_create_blueprint = Blueprint('create_product_filter_blueprint', __name__)

@product_filter_create_blueprint.route("/product_filter", methods=['POST'])
@jwt_required()
@swag_from('../../../docs/product_filter_docs/product_filter_create_docs.yaml')
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