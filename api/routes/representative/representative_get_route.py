from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from controllers.representative.representative_get_controller import get_representatives

representative_get_blueprint = Blueprint('representative_get_route', __name__)

@representative_get_blueprint.route('/representative', methods=['GET'])
@jwt_required()
def representative_get():
    return jsonify(get_representatives()), 200
