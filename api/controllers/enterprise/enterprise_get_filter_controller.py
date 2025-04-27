from models.enterprise_model import Enterprise

from flask import jsonify

def enterprise_filter(enterprise, id):
    return jsonify({
        "id": enterprise.id,
        "email": enterprise.email,
        "name": enterprise.name,
        'cnpj': enterprise.cnpj,
        "phone": enterprise.phone,
        "created_at": enterprise.created_at.isoformat()
    }), 200