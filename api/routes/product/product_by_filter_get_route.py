from flask import Blueprint
from flask_jwt_extended import jwt_required

from controllers.product.product_by_filter_get_controller import get_products_by_filters_controller
from middlewares.product.product_by_filter_get_middleware import get_products_by_filters_middleware

from flasgger.utils import swag_from

get_products_by_filters_blueprint = Blueprint('get_products_by_filters', __name__)

@get_products_by_filters_blueprint.route('/product/filters/<string:filter_ids>/', methods=['GET'])
@swag_from("../../../docs/product_docs/product_by_filter_get_docs.yaml")
@get_products_by_filters_middleware
@jwt_required()
def handle_get_products_by_filters(*args, **kwargs):
    ids = kwargs.get('ids')
    return get_products_by_filters_controller(ids)

