from models.product_filters_model import ProductFilters

def product_filter_delete_midlleware(filter_id):
    product_filter = ProductFilters.query.filter_by(filter_id=filter_id).first()

    if not product_filter:
        return "Filter not found"
    
    return None