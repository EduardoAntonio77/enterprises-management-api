from models.representative_model import Representative

def get_representative():
    response = []

    for rep in Representative.query.all():
        if not rep.enterprises:
            continue

        enterprises_data = []
        for enterprise in rep.enterprises:
            clients = [
                {
                    "client_name": c.name,
                    "client_region": c.region,
                    "client_phone": c.phone,
                    "client_cpf": c.cpf
                }
                for c in enterprise.clients
            ]

            products = [
                {
                    "product_name": p.name,
                    "product_price": p.price,
                    "product_stock": p.stock,
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

    return response
