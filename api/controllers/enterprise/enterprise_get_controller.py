from models.enterprise_model import Enterprise

def get_enterprises():
    enterprises = Enterprise.query.all()

    all_enterprises_data = []

    for enterprise in enterprises:
        client_data = {}
        for i, client in enumerate(enterprise.clients, start=1):
            client_data[str(i)] = {
                'client_name': client.name,
                'client_region': client.region,
                'client_phone': client.phone,
                'client_cpf': client.cpf
            }

        products_data = {}
        for i, product in enumerate(enterprise.products, start=1):
            filters_data = {}
            for f_i, f in enumerate(product.filters, start=1):
                filters_data[str(f_i)] = {
                    'filter_id': f.filter_id,
                    'filter_name': f.filter_name
                }

            products_data[str(i)] = {
                'product_name': product.name,
                'product_price': product.price,
                'product_stock': product.stock,
                'filters': filters_data
            }

        enterprise_data = {
            'enterprise_id': enterprise.id,
            'enterprise_name': enterprise.name,
            'enterprise_address': enterprise.address,
            'clients': client_data,
            'products': products_data
        }

        all_enterprises_data.append(enterprise_data)

    return all_enterprises_data