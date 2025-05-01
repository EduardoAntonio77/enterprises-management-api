from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from controllers.product.product_get_controller import get_products

product_get_blueprint = Blueprint('product_get_route', __name__)

@product_get_blueprint.route("/product", methods=["GET"])
@jwt_required()
@swag_from("../../../docs/product_docs/product_get_docs.yaml")
def product_get():

    return jsonify(get_products()), 200
