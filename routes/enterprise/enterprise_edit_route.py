from flask import request, jsonify, Blueprint

from middlewares.enterprise.enterprise_edit_middleware import enterprise_edit_middleware
from controllers.enterprise.enterprise_edit_controller import enterprise_edit_controller

enterprise_edit_blueprint = Blueprint('enterprise_edit_route', __name__)

@enterprise_edit_blueprint.route("/enterprise/<int:id>", methods=['PUT'])

def edit_enterprise(id):
    enterprise = enterprise_edit_middleware(id)
    if not enterprise:
        return jsonify({
            'status': 404,
            'error': 'Enterprise not found'
        }), 404
    
    data = request.get_json()
    enterprise_edit_controller(data, enterprise)

    return jsonify({
        'status': 200,
        'message': 'Enterprise updated successfully'
    }), 200
