from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from controllers.client.client_get_controller import get_clients

client_get_blueprint = Blueprint('client_get_route', __name__)

@client_get_blueprint.route("/client", methods=['GET'])
@jwt_required()
@swag_from("../../../docs/client_docs/client_get_docs.yaml")
def client_get():

    return jsonify(get_clients()), 200
