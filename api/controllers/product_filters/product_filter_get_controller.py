from models.product_filters_model import ProductFilters

def get_products_filter():
    product_filter = ProductFilters.query.all()
    return [
        {

        'filter_id': filter.filter_id,
        'filter_name': filter.filter_name,
        'created_at': filter.created_at,
        'product_id': filter.product_id

        } for filter in product_filter
    ] 