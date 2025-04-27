from flask import Blueprint, g
from controllers.client.client_get_filter_controller import client_filter
from middlewares.client.client_get_filter_middleware import client_search
from flask_jwt_extended import jwt_required

client_get_filter_blueprint = Blueprint('client_get_filter_route', __name__)

@client_get_filter_blueprint.route("/client/<int:id>", methods=['GET'])
@client_search
@jwt_required()
def client_get_filter(id, client):
    return client_filter(
        client=client, id=id
    )