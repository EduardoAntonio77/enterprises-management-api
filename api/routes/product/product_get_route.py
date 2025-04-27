from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from controllers.product.product_get_controller import get_products

product_get_blueprint = Blueprint('product_get_route', __name__)

@product_get_blueprint.route("/product", methods=["GET"])
@jwt_required()
def product_get():
    return jsonify(get_products()), 200