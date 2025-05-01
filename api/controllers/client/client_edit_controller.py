from config.database import database
from flask import jsonify

def client_edit_controller(data, client):

    if 'name' in data:
        client.name = data['name']
    if 'region' in data:
        client.region = data['region']
    if 'phone' in data:
        client.phone = data['phone']
    if 'cpf' in data:
        client.cpf = data['cpf']

    database.session.commit()

    return jsonify({
        'status': 200,
        'message': 'Client successfully updated!'
    }), 200
