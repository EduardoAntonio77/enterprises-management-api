from flask import Blueprint, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from controllers.representative.representative_get_controller import get_representatives

representative_get_blueprint = Blueprint('representative_get_route', __name__)

@representative_get_blueprint.route('/representative', methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['Representative'],
    'description': 'Endpoint para buscar todos os representantes registrados.',
    'responses': {
        200: {
            'description': 'Lista de representantes.',
            'examples': {
                'application/json': [
                    {
                        'id': 1,
                        'name': 'João da Silva',
                        'email': 'joao.silva@email.com',
                        'phone': '+55 11 91234-5678'
                    },
                    {
                        'id': 2,
                        'name': 'Maria Oliveira',
                        'email': 'maria.oliveira@email.com',
                        'phone': '+55 11 98765-4321'
                    }
                ]
            }
        },
        401: {
            'description': 'Token de autenticação inválido ou ausente.',
            'examples': {
                'application/json': {
                    'status': 401,
                    'message': 'Token de autenticação ausente ou inválido.'
                }
            }
        }
    }
})
def representative_get():
    """
    Endpoint para buscar todos os representantes.
    """
    return jsonify(get_representatives()), 200
