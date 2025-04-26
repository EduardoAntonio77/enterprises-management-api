from flask import jsonify
from models.client_model import Client
from config.database import database
from datetime import datetime, timezone
from middlewares.client.client_delete_middleware import validate_client_exists

def client_delete_controller(id):
    error = validate_client_exists(id)
    if error:
        return jsonify({
            'error': error
            }), 404

    client = Client.query.get(id)
    client.deleted_at = datetime.now(timezone.utc)

    database.session.commit()

    return jsonify({
        'status': 200,
        'message': f'Client {id} deleted successfully'
        }), 200
