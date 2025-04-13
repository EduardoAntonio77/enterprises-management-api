# imports
from flask import Blueprint, request, jsonify;

from database import database;
from models.representative_model import Representative;
from middlewares.representative_create_middleware import validate_representant_data;

create_representant_blueprint = Blueprint('create_representant_blueprint', __name__)

# register representatives
@create_representant_blueprint.route('/representative', methods=['POST'])
def register_representative():
    # data é os dados q o usuário fez post
    data = request.json;
    error = validate_representant_data(data) # aqui a gente passa o data pro middleware validar os campos necessários

    # se houver erro, retornar esse json
    if error:
        return jsonify({
            "status": 400,
            "message": error,
        }), 400;

    new_representative = Representative(
       name=data['name'],
       cnpj=data['cnpj'],
       email=data['email'],
       phone=data['phone'],
    );

    database.session.add(new_representative);
    database.session.commit();
    
    return jsonify({
        'status': 200,
        'message': 'Successfully registered representative!'
    });