from models.product_model import Product

def get_products():

    response = []

    for prod in Product.query.filter(Product.deleted_at.is_(None)).all():

        product_filters_data = [{
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
            'filters': [
                product_filters_data
            ]
        }
        
        response.append(products_data)

    return response
