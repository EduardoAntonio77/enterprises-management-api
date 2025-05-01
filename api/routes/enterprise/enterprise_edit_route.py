from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from

# Importando middlewares e controllers
from middlewares.enterprise.enterprise_edit_middleware import enterprise_edit_middleware
from controllers.enterprise.enterprise_edit_controller import enterprise_edit_controller

# Criando blueprint para a rota
enterprise_edit_blueprint = Blueprint('enterprise_edit_route', __name__)

@enterprise_edit_blueprint.route("/enterprise/<int:id>", methods=['PUT'])
@jwt_required()
@swag_from("../../../docs/enterprise_docs/enterprise_edit_docs.yaml")
def edit_enterprise(id):
    
    enterprise = enterprise_edit_middleware(id)
    if not enterprise:
        return jsonify({
        'status': 404,
        'message': 'Enterprise not found'
    }), 404
    
    data = request.get_json()

    enterprise_edit_controller(enterprise, data)

    return jsonify({
        'status': 200,
        'message': 'Enterprise updated successfully'
    }), 200