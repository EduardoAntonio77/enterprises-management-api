# imports
from flask import Blueprint, request, jsonify;

# Importando middlewares e controllers
from middlewares.enterprise.enterprise_create_middleware import enterprise_create;
from controllers.enterprise.enterprise_create_controller import create_enterprise;

# Criando um blueprint para registrar a rota em app.py
create_enterprise_blueprint = Blueprint('create_enterprise_blueprint', __name__)
@create_enterprise_blueprint.route('/enterprise', methods=['POST'])
def register_enterprise():
    # Criando uma variavel que ira receber os dados que o usuario passou na rota usando o metodo POST.
    data = request.json;

    error = enterprise_create(data)
    if error:
        return jsonify({
            'status': 400,
            'error': error
        }), 400;

    create_enterprise(data)

    return jsonify({
        'status': 200,
        'message': "Successfully registered enterprise"
    })
