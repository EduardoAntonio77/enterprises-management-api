from flask import Blueprint, jsonify
from flasgger import swag_from

slash_blueprint = Blueprint('slash_blueprint', __name__)

# Slash route
@slash_blueprint.route('/')
@swag_from({
    'tags': ['Home page'],
    'description': 'Endpoint raiz que retorna informações sobre o banco de dados de empresas.',
    'responses': {
        200: {
            'description': 'Informações do banco de dados de empresas retornadas com sucesso!',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Enterprises Database',
                    'version': 0.1
                }
            }
        }
    }
})
def slashroute():
    """
    Endpoint raiz que retorna informações sobre o banco de dados de empresas
    """
    return jsonify({
        'status': 200,
        'message': 'Enterprises Database',
        'version': 0.1
    })
