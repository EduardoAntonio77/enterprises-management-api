from flask import Blueprint, g
from middlewares.representative.representative_get_filter_middleware import representative_search
from flask_jwt_extended import jwt_required
from controllers.representative.representative_get_filter_controller import representative_filter

representative_get_filter_blueprint = Blueprint('representative_get_filter_route', __name__)

@representative_get_filter_blueprint.route("/representative/<int:id>", methods=["GET"])
@representative_search
@jwt_required()
def representative_get_filter(id, representative):
    return representative_filter(representative=representative, id=id)

