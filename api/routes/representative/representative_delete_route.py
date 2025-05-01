from flask import jsonify, Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from

from middlewares.representative.representative_delete_middleware import representative_delete_middleware
from controllers.representative.representative_delete_controller import delete_representative_controller

delete_representative_blueprint = Blueprint("representative_routes", __name__)

@delete_representative_blueprint.route('/representative/<int:id>', methods=['DELETE'])
@jwt_required()
@swag_from("../../../docs/representative_docs/representative_delete_docs.yaml")
def delete_representative(id):

    error = representative_delete_middleware(id)

    if error:
        return jsonify({
            "status": 400,
            "message": error,
        }), 400

    delete_representative_controller(id)

    return jsonify({
        'status': 200,
        'message': 'Representative successfully deleted!'
    }), 200
