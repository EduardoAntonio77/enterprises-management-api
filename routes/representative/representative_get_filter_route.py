from flask import Blueprint, jsonify
from middlewares.representative.representative_get_filter_middleware import representative_search
from flask_jwt_extended import jwt_required

representative_get_filter_blueprint = Blueprint('representative_get_filter_route', __name__)

@representative_get_filter_blueprint.route("/representative/<int:id>", methods=["GET"])
@representative_search  # Aplica o middleware antes da rota
@jwt_required()
def representative_filter(representative, id):  # O 'representative' é passado pelo middleware
    return jsonify({
        "id": representative.id,
        "email": representative.email,
        "name": representative.name,
        'cnpj': representative.cnpj,
        "phone": representative.phone,
        "created_at": representative.created_at.isoformat()
    }), 200
