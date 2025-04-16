from flask import jsonify, Blueprint;

from middlewares.enterprise.enterprise_delete_middleware import enterprise_delete_middleware;
from controllers.enterprise.enterprise_delete_controller import enterprise_delete_controller;

enterprise_delete_blueprint = Blueprint('enterprise_delete_route', __name__)

@enterprise_delete_blueprint.route('/enterprise/<int:id>', methods=['DELETE'])
def delete_enterprise(id):
    error = enterprise_delete_middleware(id)
    
    if error:
        return jsonify({
            'status': 400,
            'message': error
        }), 400;

    enterprise_delete_controller(id)
    return jsonify({
        'status': 200,
        'message': 'Representative successfully deleted!'
    }), 200;