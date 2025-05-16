from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from controllers.product_filters.product_filter_get_controller import get_products_filter

from flasgger.utils import swag_from

product_filter_get_blueprint = Blueprint("product_filter_get_route", __name__)

@product_filter_get_blueprint.route("/product_filter", methods=["GET"])
@jwt_required()
@swag_from("../../../docs/product_filter_docs/product_filter_get_docs.yaml")
def product_filter_get():

    return jsonify(get_products_filter()), 200