from flask import jsonify
from config.database import database

def edit_representative_controller(repre, data):
    
    if 'name' in data:
        repre.name = data['name']
    if 'cnpj' in data:
        repre.cnpj = data['cnpj']
    if 'email' in data:
        repre.email = data['email']
    if 'phone' in data:
        repre.phone = data['phone']
    
   
    database.session.commit()

   
    return jsonify({
        'status': 200,
        'message': 'Representative successfully updated!'
    }), 200
