from models.client_model import Client
from flask import jsonify

def client_filter(client, id):
    return jsonify({
        "id": client.id,
        "name": client.name,
        "region": client.region,
        "phone": client.phone,
        "cpf": client.cpf,
        "created_at": client.created_at.isoformat()
    }), 200