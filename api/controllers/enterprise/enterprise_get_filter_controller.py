from flask import jsonify

def enterprise_filter(enterprise, id):
    return jsonify({
        "id": enterprise.id,
        "client_quantity": enterprise.client_quantity,
        "name": enterprise.name,
        'address': enterprise.address,
        "phone": enterprise.phone,
        "created_at": enterprise.create_at.isoformat()
    }), 200