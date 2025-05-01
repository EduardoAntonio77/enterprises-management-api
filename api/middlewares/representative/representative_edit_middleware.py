from models.representative_model import Representative
from flask import jsonify

def representative_middleware(id):
    
    representative = Representative.query.get(id)

    if not representative:
        return jsonify({
            "status": 404,
            "error": "Representative not found"
        }), 404
    
    return representative
