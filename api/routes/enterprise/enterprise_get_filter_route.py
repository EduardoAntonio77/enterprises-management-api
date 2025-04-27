from flask import Blueprint, g
from middlewares.enterprise.enterprise_get_filter_middleware import enterprise_search
from flask_jwt_extended import jwt_required
from controllers.enterprise.enterprise_get_filter_controller import enterprise_filter   

enterprise_get_filter_blueprint = Blueprint('enterprise_get_filter_route', __name__)

@enterprise_get_filter_blueprint.route('/enterprise/<int:id>', methods=['GET'])
@enterprise_search
@jwt_required()
def enterprise_get_filter(id, enterprise):
    return enterprise_filter(enterprise=enterprise, id=id)