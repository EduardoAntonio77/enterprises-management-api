from flask import jsonify, Blueprint
from flask_jwt_extended import jwt_required
from flasgger import swag_from

from middlewares.representative.representative_delete_middleware import representative_delete_middleware
from controllers.representative.representative_delete_controller import delete_representative_controller

delete_representative_blueprint = Blueprint("representative_routes", __name__)

@delete_representative_blueprint.route('/representative/<int:id>', methods=['DELETE'])
@jwt_required()
@swag_from({
    'tags': ['Representative'],
    'description': 'Endpoint para excluir um representante pelo ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do representante a ser excluído',
            'example': 1
        }
    ],
    'responses': {
        200: {
            'description': 'Representante excluído com sucesso!',
            'examples': {
                'application/json': {
                    'status': 200,
                    'message': 'Representative successfully deleted!'
                }
            }
        },
        400: {
            'description': 'Erro ao tentar excluir o representante.',
            'examples': {
                'application/json': {
                    'status': 400,
                    'message': 'Erro: Representante não encontrado.'
                }
            }
        }
    }
})
def delete_representative(id):
    """
    Endpoint para excluir um representante.
    """

    error = representative_delete_middleware(id)

    if error:
        return jsonify({
            "status": 400,
            "message": error,
        }), 400

    delete_representative_controller(id)

    return jsonify({
        'status': 200,
        'message': 'Representative successfully deleted!'
    }), 200
