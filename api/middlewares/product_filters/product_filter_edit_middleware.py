from models.product_filters_model import ProductFilters
from models.product_model import Product

def product_filter_edit(data, filter_id):
    product_filter = ProductFilters.query.filter_by(filter_id=filter_id).first()
    if not product_filter:
        return 'Filter not found'
    
    if 'product_id' in data:
        product = Product.query.filter_by(product_id=data['product_id']).first()
        if not product:
            return 'Product not found'
        
    return product_filter