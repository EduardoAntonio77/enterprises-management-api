from flask import Blueprint, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from controllers.representative.representative_get_controller import get_representatives

representative_get_blueprint = Blueprint('representative_get_route', __name__)

@representative_get_blueprint.route('/representative', methods=['GET'])
@jwt_required()
@swag_from("../../../docs/representative_docs/representative_get_docs.yaml")
def representative_get():

    return jsonify(get_representatives()), 200
