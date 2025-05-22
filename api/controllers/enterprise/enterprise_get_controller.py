from models.enterprise_model import Enterprise
from flask import request
import json

def get_enterprises():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 3, type=int)

    pagination = Enterprise.query.order_by(Enterprise.id).paginate(page=page,per_page=per_page,error_out=False)

    enterprises = pagination.items

    enterprise_data = [
        {
            'enterprise_id': e.id,
            'enterprise_name': e.name,
            'enterprise_address': e.address,
            'clients': [
                {
                    'client_id': c.id,
                    'client_name': c.name,
                    'client_region': c.region,
                    'client_phone': c.phone,
                    'client_cpf': c.cpf
                } for c in e.clients
            ],
            'products': [
                {
                    'product_id': p.id,
                    'product_name': p.name,
                    'product_price': p.price,
                    'product_stock': p.stock,
                    'filters': [
                        {
                            'filter_id': f.filter_id,
                            'filter_name': f.filter_name
                        } for f in sorted(p.filters, key=lambda f: f.filter_id)
                    ]
                } for p in sorted(e.products, key=lambda p: p.id)
            ]
        } for e in enterprises
    ]

    result = {
        'page': pagination.page,
        'per_page': pagination.per_page,
        'total_pages': pagination.pages,
        'total_items': pagination.total,
        'data': enterprise_data
    }

    print(json.dumps(result, indent=4))

    return result
