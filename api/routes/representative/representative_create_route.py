# imports
from flask import Blueprint, request, jsonify
from flasgger import swag_from

# importando middleware e controller
from middlewares.representative.representative_create_middleware import validate_representant_data
from controllers.representative.representative_create_controller import register_representative_controller

# criando blueprint
create_representant_blueprint = Blueprint('create_representant_blueprint', __name__)

@create_representant_blueprint.route('/representative', methods=['POST'])
@swag_from("../../../docs/representative_docs/representative_create_docs.yaml")
def register_representative():


    data = request.json

    error = validate_representant_data(data)

    if error:
        return jsonify({
            "status": 400,
            "message": error,
        }), 400

    register_representative_controller(data)

    return jsonify({
        'status': 200,
        'message': 'Successfully registered representative!'
    })
