from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from controllers.client.client_get_controller import get_clients

client_get_blueprint = Blueprint('client_get_route', __name__)

@client_get_blueprint.route("/client", methods=['GET'])
@jwt_required()
def client_get():
    return jsonify(get_clients()), 200