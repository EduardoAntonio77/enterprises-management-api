from models.representative_model import Representative
from flask import request
import json

def get_representative():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 3, type=int)

    pagination = Representative.query.order_by(Representative.id).paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    reps = pagination.items

    response = []

    for rep in reps:
        if not rep.enterprises:
            continue

        enterprises_data = []
        for enterprise in rep.enterprises:
            clients = [
                {
                    "client_id": c.id,
                    "client_name": c.name,
                    "client_region": c.region,
                    "client_phone": c.phone,
                    "client_cpf": c.cpf
                }
                for c in enterprise.clients
            ]

            products = [
                {
                    "product_id": p.id,
                    "product_name": p.name,
                    "product_price": p.price,
                    "product_stock": p.stock,
                    "enterprise_id": p.enterprise_id,
                    "filters": [
                        {
                            "filter_id": f.filter_id,
                            "filter_name": f.filter_name
                        } for f in p.filters
                    ]
                }
                for p in enterprise.products
            ]

            enterprises_data.append({
                "enterprise_id": enterprise.id,
                "enterprise_name": enterprise.name,
                "enterprise_address": enterprise.address,
                "clients": clients,
                "products": products
            })

        rep_data = {
            "id": rep.id,
            "name": rep.name,
            "cnpj": rep.cnpj,
            "email": rep.email,
            "enterprises": enterprises_data
        }

        response.append(rep_data)

    result = {
        'page': pagination.page,
        'per_page': pagination.per_page,
        'total_pages': pagination.pages,
        'total_items': pagination.total,
        'data': response
    }

    print(json.dumps(result, indent=4))

    return result
