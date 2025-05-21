from models.client_model import Client

def get_clients():
    clients = Client.query.filter(Client.deleted_at.is_(None)).all()
    response = []

    for client in clients:
        client_data = {
            'client_id': client.id,
            'client_name': client.name,
            'client_region': client.region,
            'client_phone': client.phone,
            'client_cpf': client.phone,
            'enterprise_id': client.enterprise_id
        }
        response.append(client_data)

    return response
    
