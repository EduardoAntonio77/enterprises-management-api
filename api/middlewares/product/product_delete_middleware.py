from models.product_model import Product

def product_delete(product_id):
    product = Product.query.filter_by(id=product_id).first()
    
    if not product:
        return "Product not found"
    
    return None
