from models.product_model import Product
from flask import request
import json

def get_products():
    page = request.args.get('page', 1, type=int)          
    per_page = request.args.get('per_page', 3, type=int)  

    pagination = Product.query.filter(Product.deleted_at.is_(None)).order_by(Product.id).paginate(page=page,per_page=per_page,error_out=False)

    products = pagination.items

    response = []

    for prod in products:
        product_filters_data = [
            {
                'filter_id': fil.filter_id,
                'filter_name': fil.filter_name
            }
            for fil in prod.filters
        ]

        products_data = {
            'product_id': prod.id,
            'product_name': prod.name,
            'product_price': prod.price,
            'product_stock': prod.stock,
            'enterprise_id': prod.enterprise_id,
            'filters': product_filters_data
        }

        response.append(products_data)

    result = {
        'page': pagination.page,
        'per_page': pagination.per_page,
        'total_pages': pagination.pages,
        'total_items': pagination.total,
        'data': response
    }

    print(json.dumps(result, indent=4))

    return result
