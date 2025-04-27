from flask import jsonify
from models.product_model import Product
from functools import wraps

def product_search(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        id = kwargs.get('id')

        if id is None:
            return jsonify({'error': 'ID é obrigatório'}), 400
        
        rep = Product.query.filter_by(id=id, deleted_at=None).first()
        if not rep:
            return jsonify({'error': 'Produto não encontrado'}), 404
        
        kwargs['product'] = rep
        
        return func(*args, **kwargs)
    
    return wrapper