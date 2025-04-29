from flask import request, Blueprint, jsonify
from flasgger import swag_from
from middlewares.representative.representative_edit_middleware import representative_middleware
from flask_jwt_extended import jwt_required
from controllers.representative.representative_edit_controller import edit_representative_controller

edit_representative_blueprint = Blueprint('edit_representative_route', __name__) # Criando um blueprint para a rota.

@edit_representative_blueprint.route('/representative/<int:id>', methods=['PUT']) # Criando uma rota que aceitará apenas o uso de métodos PUT que converterá para um valor int, o valor passado na query.
@jwt_required()
@swag_from({
    'tags': ['Representative'],
    'description': 'Endpoint para editar um representante existente.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do representante a ser editado',
            'example': 123
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'João da Silva'},
                    'email': {'type': 'string', 'example': 'joao@email.com'},
                    'phone': {'type': 'string', 'example': '+55 11 91234-5678'}
                },
                'required': ['name', 'email', 'phone']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Representante editado com sucesso!',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Representative successfully updated!'
                }
            }
        },
        404: {
            'description': 'Representante não encontrado.',
            'examples': {
                'application/json': {
                    'status': 404,
                    'message': 'Representative not found'
                }
            }
        },
        400: {
            'description': 'Erro na validação dos dados enviados.',
            'examples': {
                'application/json': {
                    'status': 400,
                    'message': 'Erro: Dados do representante inválidos.'
                }
            }
        }
    }
})
def edit_representative(id):
    """
    Endpoint para editar um representante.
    """

    repre = representative_middleware(id)  # Verificando se o representante existe.

    data = request.json

    if not repre:
        return jsonify({
            "status": 404,
            "error": "Representative not found"
        }), 404  # Caso o representante não seja encontrado, retorna erro 404
    
    return edit_representative_controller(repre, data)
