from flask import Blueprint, jsonify
from flasgger import swag_from

slash_blueprint = Blueprint('slash_blueprint', __name__)

# Slash route
@slash_blueprint.route('/')
@swag_from("../../docs/slash_route_docs.yaml")
def slash_route():
    return jsonify({
        'status': 200,
        'message': 'Enterprises Database',
        'version': 0.1
    })
