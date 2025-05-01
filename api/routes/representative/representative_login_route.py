from flask import Blueprint, jsonify, g
from flasgger import swag_from
from middlewares.representative.representative_login_middleware import login_required
from controllers.representative.representative_login_controller import representative_login

login_route = Blueprint("representative_login_route", __name__)

@login_route.route("/login", methods=["POST"])
@login_required
@swag_from("../../docs/login_route_docs.yaml")
def login():

    login = representative_login()

    return jsonify(login), 200
