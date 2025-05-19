from models.representative_model import Representative
from collections import OrderedDict  # opcional

def get_representative():
    representatives = Representative.query.all()
    response = []

    for rep in representatives:
        if not rep.enterprises:
            continue

        enterprise = rep.enterprises[0]  # se usar apenas a primeira

        # Clients
        clients_data = {}
        for idx, client in enumerate(enterprise.clients, start=1):
            clients_data[str(idx)] = {
                "client_name": client.name,
                "client_region": client.region,
                "client_phone": client.phone,
                "client_cpf": client.cpf
            }

        # Products
        products_data = {}
        for idx, product in enumerate(enterprise.products, start=1):
            filters_data = {}
            for jdx, f in enumerate(product.filters, start=1):
                filters_data[str(jdx)] = {
                    "filter_id": f.filter_id,
                    "filter_name": f.filter_name
                }

            products_data[str(idx)] = {
                "product_name": product.name,
                "product_price": product.price,
                "product_stock": product.stock,
                "filters": filters_data
            }

        # Representante + empresa
        rep_data = OrderedDict()  # se quiser garantir ordem
        rep_data["id"] = rep.id
        rep_data["name"] = rep.name
        rep_data["cnpj"] = rep.cnpj
        rep_data["email"] = rep.email
        rep_data["enterprise"] = OrderedDict({
            "enterprise_id": enterprise.id,
            "enterprise_name": enterprise.name,
            "enterprise_address": enterprise.address,
            "clients": clients_data,
            "products": products_data
        })

        response.append(rep_data)

    return response
