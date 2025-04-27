from flask import jsonify
from models.client_model import Client
from functools import wraps

def client_search(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        id = kwargs.get('id')

        if id is None:
            return jsonify({'error': 'ID é obrigatório'}), 400
        
        rep = Client.query.filter_by(id=id, deleted_at=None).first()
        if not rep:
            return jsonify({'error': 'Client não encontrado'}), 404
        
        kwargs['client'] = rep
        
        return func(*args, **kwargs)
    
    return wrapper