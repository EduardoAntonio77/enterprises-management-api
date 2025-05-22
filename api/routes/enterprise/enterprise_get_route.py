from flask import Blueprint, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from controllers.enterprise.enterprise_get_controller import get_enterprises

enterprise_get_blueprint = Blueprint('enterprise_get_route', __name__)

@enterprise_get_blueprint.route('/enterprise', methods=['GET'])
@jwt_required()
@swag_from("../../../docs/enterprise_docs/enterprise_get_docs.yaml")
def enterprise_get():

    return jsonify(get_enterprises()), 200
