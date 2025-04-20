from flask import jsonify
from models.representative_model import Representative
from functools import wraps

def representative_search(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        id = kwargs.get('id')

        if id is None:
            return jsonify({'error': 'ID é obrigatório'}), 400
        
        rep = Representative.query.filter_by(id=id, delete_at=None).first()
        if not rep:
            return jsonify({'error': 'Representante não encontrado'}), 404
        
        kwargs['representative'] = rep
        
        return func(*args, **kwargs)
    
    return wrapper
