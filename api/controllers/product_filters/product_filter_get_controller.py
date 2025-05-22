from models.product_filters_model import ProductFilters
from flask import request
import json

def get_products_filter():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    pagination = ProductFilters.query.order_by(ProductFilters.filter_id).paginate(page=page,per_page=per_page,error_out=False)

    product_filters = pagination.items

    product_data = [
        {
            'filter_id': pf.filter_id,
            'filter_name': pf.filter_name,
            'product_id': pf.product_id
        } for pf in product_filters
    ]

    result = {
        'page': pagination.page,
        'per_page': pagination.per_page,
        'total_pages': pagination.pages,
        'total_items': pagination.total,
        'data': product_data
    }

    print(json.dumps(result, indent=4))
    return result
