from models.product_model import Product
from models.enterprise_model import Enterprise

def product_edit(data, id):
    product = Product.query.filter_by(id=id, deleted_at=None).first()
    if not product:
        return "Product not found"

    if 'enterprise_id' in data:
        enterprise = Enterprise.query.filter_by(id=data['enterprise_id']).first()
        if not enterprise:
            return "Enterprise not found"

    return None
