from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flasgger import swag_from

# Importando middlewares e controllers
from middlewares.enterprise.enterprise_create_middleware import enterprise_create
from controllers.enterprise.enterprise_create_controller import create_enterprise

# Criando um blueprint para registrar a rota em app.py
create_enterprise_blueprint = Blueprint('create_enterprise_blueprint', __name__)

@create_enterprise_blueprint.route('/enterprise', methods=['POST'])
@jwt_required()
@swag_from("../../../docs/enterprise_docs/enterprise_create_docs.yaml")
def register_enterprise():

    # Dados recebidos via POST
    data = request.json

    # Validando os dados com middleware
    error = enterprise_create(data)
    if error:
        return jsonify({
            'status': 400,
            'error': error
        }), 400

    # Criando a empresa através do controller
    create_enterprise(data)

    return jsonify({
        'status': 200,
        'message': "Successfully registered enterprise"
    })
