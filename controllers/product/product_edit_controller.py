from database import database
from models.product_model import Product

def product_edit_controller(id, data):
    product = Product.query.filter_by(id=id, deleted_at=None).first()
    if not product:
        return "Product not found"

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
