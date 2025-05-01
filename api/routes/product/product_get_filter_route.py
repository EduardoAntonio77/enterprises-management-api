from flask import Blueprint, g
from flasgger import swag_from
from middlewares.product.product_get_filter_middleware import product_search
from controllers.product.product_get_filter_controller import product_filter
from flask_jwt_extended import jwt_required

product_get_filter_blueprint = Blueprint("product_get_filter_route", __name__)

@product_get_filter_blueprint.route("/product/<int:id>", methods=["GET"])
@product_search
@jwt_required()
@swag_from("../../../docs/product_docs/product_get_filter_docs.yaml")
def product_get(id, product):

    return product_filter(product=product, id=id)
