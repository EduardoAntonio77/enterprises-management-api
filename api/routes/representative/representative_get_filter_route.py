from flask import Blueprint, g
from flasgger import swag_from
from middlewares.representative.representative_get_filter_middleware import representative_search
from flask_jwt_extended import jwt_required
from controllers.representative.representative_get_filter_controller import representative_filter

representative_get_filter_blueprint = Blueprint('representative_get_filter_route', __name__)

@representative_get_filter_blueprint.route("/representative/<int:id>", methods=["GET"])
@representative_search
@jwt_required()
@swag_from({
    'tags': ['Representative'],
    'description': 'Endpoint para buscar um representante com base em filtros.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do representante que será filtrado.',
            'example': 123
        }
    ],
    'responses': {
        200: {
            'description': 'Representante encontrado com sucesso!',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Representante encontrado!',
                    'representative': {
                        'id': 123,
                        'name': 'João da Silva',
                        'email': 'joao@email.com',
                        'phone': '+55 11 91234-5678'
                    }
                }
            }
        },
        404: {
            'description': 'Representante não encontrado.',
            'examples': {
                'application/json': {
                    'status': 404,
                    'message': 'Representante não encontrado.'
                }
            }
        }
    }
})
def representative_get_filter(id, representative):
    """
    Endpoint para buscar um representante com base em filtros.
    """
    return representative_filter(representative=representative, id=id)
