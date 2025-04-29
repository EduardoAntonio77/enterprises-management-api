# imports
from flask import Blueprint, request, jsonify
from flasgger import swag_from

# importando middleware e controller
from middlewares.representative.representative_create_middleware import validate_representant_data
from controllers.representative.representative_create_controller import register_representative_controller

# criando blueprint
create_representant_blueprint = Blueprint('create_representant_blueprint', __name__)

@create_representant_blueprint.route('/representative', methods=['POST'])
@swag_from({
    'tags': ['Representative'],
    'description': 'Endpoint para registrar um novo representante na empresa.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'João da Silva'},
                    'email': {'type': 'string', 'example': 'joao@email.com'},
                    'phone': {'type': 'string', 'example': '+55 11 91234-5678'},
                    'password': {'type': 'string', 'example': 'joao1234'}
                },
                'required': ['name', 'email', 'phone', 'password']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Representante registrado com sucesso!',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Successfully registered representative!'
                }
            }
        },
        400: {
            'description': 'Erro na validação dos dados enviados.',
            'examples': {
                'application/json': {
                    'status': 400,
                    'message': 'Campo "email" é obrigatório.'
                }
            }
        }
    }
})
def register_representative():
    """
    Endpoint para criação de representantes.
    """

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
