from flask import Blueprint, g
from flask_jwt_extended import jwt_required
from flasgger import swag_from
from controllers.client.client_get_filter_controller import client_filter
from middlewares.client.client_get_filter_middleware import client_search

client_get_filter_blueprint = Blueprint('client_get_filter_route', __name__)

@client_get_filter_blueprint.route("/client/<int:id>", methods=['GET'])
@client_search
@jwt_required()
@swag_from("../../../docs/client_docs/client_get_filter_docs.yaml")
def client_get_filter(id, client):

    return client_filter(
        client=client, id=id
    )
