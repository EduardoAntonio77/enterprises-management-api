from models.client_model import Client
from flask import request
import json

def get_clients():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 3, type=int)

    pagination = Client.query.filter(
        Client.deleted_at.is_(None)
    ).order_by(Client.id).paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    clients = pagination.items

    response = []

    for client in clients:
        client_data = {
            'client_id': client.id,
            'client_name': client.name,
            'client_region': client.region,
            'client_phone': client.phone,
            'client_cpf': client.cpf,
            'enterprise_id': client.enterprise_id
        }
        response.append(client_data)

    result = {
        'page': pagination.page,
        'per_page': pagination.per_page,
        'total_pages': pagination.pages,
        'total_items': pagination.total,
        'data': response
    }

    print(json.dumps(result, indent=4))
    return result
