from flask import request, Blueprint, jsonify
from flasgger import swag_from
from middlewares.representative.representative_edit_middleware import representative_middleware
from flask_jwt_extended import jwt_required
from controllers.representative.representative_edit_controller import edit_representative_controller

edit_representative_blueprint = Blueprint('edit_representative_route', __name__) # Criando um blueprint para a rota.

@edit_representative_blueprint.route('/representative/<int:id>', methods=['PUT']) # Criando uma rota que aceitará apenas o uso de métodos PUT que converterá para um valor int, o valor passado na query.
@jwt_required()
@swag_from("../../../docs/representative_docs/representative_edit_docs.yaml")
def edit_representative(id):

    repre = representative_middleware(id)  # Verificando se o representante existe.

    data = request.json
 
    return edit_representative_controller(repre, data)
