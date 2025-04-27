from flask import jsonify
from models.enterprise_model import Enterprise
from functools import wraps

def enterprise_search(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        id = kwargs.get('id')

        if id is None:
            return jsonify({'error': 'ID é obrigatório'}), 400
        
        rep = Enterprise.query.filter_by(id=id, deleted_at=None).first()
        if not rep:
            return jsonify({'error': 'Empresa não encontrada'}), 404
        
        kwargs['enterprise'] = rep
        
        return func(*args, **kwargs)
    
    return wrapper