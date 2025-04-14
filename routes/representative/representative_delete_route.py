# imports
from flask import jsonify, Blueprint;

# middlewares & controllers
from middlewares.representative.representative_delete_middleware import representative_delete_middleware;
from controllers.representative_delete_controller import delete_representative_controller;

# Criando um blueprint para a rota.
delete_representative_blueprint = Blueprint("representative_routes", __name__); 

# Criando uma rota que utilizara apenas o método DELETE, ela ira converter o trecho "<int:id>" da URL para um int e manda como argumento para a função usa-la.
@delete_representative_blueprint.route('/representative/<int:id>', methods=['DELETE']) 
def delete_representative(id):
    # chamando middleware
    error = representative_delete_middleware(id)
    # se o middleware retornar qualquer coisa != de None...
    if error:
        return jsonify({
            "status": 400,
            "message": error,
        }), 400;

    # se o middleware não retornar nada (ou seja: não retornar erro), chamar o controller
    delete_representative_controller(id)
    return jsonify({
        'status': 200,
        'message': 'Representative successfully deleted!'
    }), 200;


