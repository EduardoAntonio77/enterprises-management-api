from models.product_model import Product

def get_products():
    products = Product.query.filter(Product.deleted_at.is_(None)).all()
    return [
        {
        'id': prod.id,
        'name': prod.name,
        'enterprise_id': prod.enterprise_id

        } for prod in products
    ]