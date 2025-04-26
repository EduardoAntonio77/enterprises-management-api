from models.representative_model import Representative

from flask import jsonify

def representative_filter(representative, id):
    return jsonify({
        "id": representative.id,
        "email": representative.email,
        "name": representative.name,
        'cnpj': representative.cnpj,
        "phone": representative.phone,
        "created_at": representative.created_at.isoformat()
    }), 200
