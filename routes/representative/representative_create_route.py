# imports
from flask import Blueprint, request, jsonify;
from models.representative_model import Representative;

# importando middleware e controller
from middlewares.representative.representative_create_middleware import validate_representant_data;
from controllers.representative_create_controller import register_representative_controller;

# criando blueprint
create_representant_blueprint = Blueprint('create_representant_blueprint', __name__)
@create_representant_blueprint.route('/representative', methods=['POST'])
def register_representative():
    # data é os dados q o usuário fez post
    data = request.json;
    # usando middleware
    error = validate_representant_data(data) # aqui a gente passa o data pro middleware validar os campos necessários

    # se houver erro, retornar esse json
    if error:
        return jsonify({
            "status": 400,
            "message": error,
        }), 400;

    # usando controller se não houver erro:
    register_representative_controller(data)
    
    return jsonify({
        'status': 200,
        'message': 'Successfully registered representative!'
    });