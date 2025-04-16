from flask import jsonify, Blueprint
from middlewares.representative.representative_edit_middleware import representative_middleware

edit_representative_blueprint = Blueprint('edit_representative_route', __name__) # Criando um blueprint para a rota.

@edit_representative_blueprint.route('/representative/<int:id>', methods=['PUT']) # Criando uma rota que aceitara apenas o uso de métodos PUT que convertera para um valor int, o valor passado na query.

def edit_representative(id): # Criando uma função que sera executada aoacessar a rota.

    repre = representative_middleware(id) # Criando uma variavel que recebera um chamado para a função importada no inicio do código.
    if not repre:
        return jsonify({
            "status": 404,
            "error": "Representative not found"
        }), 404 # Caso o o representante com o id informado não exista, retornara uma respota json informando um erro 404 (not found)