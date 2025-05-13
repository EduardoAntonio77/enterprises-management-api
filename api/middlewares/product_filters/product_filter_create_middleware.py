from models.product_filters_model import ProductFilters
from models.product_model import Product

def product_filters_create(data):
    required_fields = ['filter_name', 'product_id']
    for field in required_fields:
        if field not in data:
            return f"Missing field: {field}"
        
    product = Product.query.filter_by(id=data["product_id"]).first()

    if not product:
        return "Product not found"
    
    return None