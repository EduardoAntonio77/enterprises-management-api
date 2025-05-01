from flask import jsonify, Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from

# Importando middlewares e controllers
from middlewares.enterprise.enterprise_delete_middleware import enterprise_delete_middleware
from controllers.enterprise.enterprise_delete_controller import enterprise_delete_controller

# Criando blueprint para a rota
enterprise_delete_blueprint = Blueprint('enterprise_delete_route', __name__)

@enterprise_delete_blueprint.route('/enterprise/<int:id>', methods=['DELETE'])
@jwt_required()
@swag_from("../../../docs/enterprise_docs/enterprise_delete_docs.yaml")
def delete_enterprise(id):

    error = enterprise_delete_middleware(id)
    
    if error:
        return jsonify({
            'status': 400,
            'message': error
        }), 400

    # Chama o controller para efetuar a exclusão
    enterprise_delete_controller(id)
    
    return jsonify({
        'status': 200,
        'message': 'Representative successfully deleted!'  # Corrigir a mensagem, se necessário
    }), 200
