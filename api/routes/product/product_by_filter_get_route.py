from flask import Blueprint
from controllers.product.product_by_filter_get_controller import get_products_by_filters_controller
from middlewares.product.product_by_filter_get_middleware import get_products_by_filters_middleware
from flask_jwt_extended import jwt_required

get_products_by_filters_blueprint = Blueprint('get_products_by_filters', __name__)

@get_products_by_filters_blueprint.route('/product/filters', methods=['GET'])
@get_products_by_filters_middleware
@jwt_required()
def handle_get_products_by_filters():
    return get_products_by_filters_controller()
