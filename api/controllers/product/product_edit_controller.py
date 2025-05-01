from config.database import database
from models.product_model import Product
from flask import jsonify

def product_edit_controller(product, data):
    if 'name' in data:
        product.name = data['name']
    if 'price' in data:
        product.price = float(data['price'])
    if 'stock' in data:
        product.stock = int(data['stock'])
    if 'enterprise_id' in data:
        product.enterprise_id = int(data['enterprise_id'])

   
    database.session.commit()

    return None
