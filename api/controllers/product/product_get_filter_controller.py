from models.product_model import Product
from flask import jsonify

def product_filter(product, id):
    return jsonify({
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "stock": product.stock,
        "enterprise_id": product.enterprise_id,
        "created_at": product.created_at.isoformat()
    })