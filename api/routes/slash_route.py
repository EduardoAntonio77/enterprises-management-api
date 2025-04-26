# imports
from flask import Blueprint, jsonify;

slash_blueprint = Blueprint('slash_blueprint', __name__)

# slash route
@slash_blueprint.route('/')
def slashroute():
    return jsonify({
        'status': 200,
        'message': 'Enterprises Database',
        'version': 0.1
    });