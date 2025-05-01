# Imports
from config.database import database 
from flask import jsonify
def enterprise_edit_controller(enterprise, data):

    if 'name' in data:
        enterprise.name = data['name']
    if 'client_quantity' in data:
        enterprise.client_quantity = data['client_quantity']
    if 'address' in data:
        enterprise.address = data['address']
    if 'phone' in data:
        enterprise.phone = data['phone']

    database.session.commit()


    return jsonify({
        'status': 200,
        'message': 'Enterprise successfully updated!'
    }), 200
