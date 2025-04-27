from models.client_model import Client

def get_clients():
    clients = Client.query.filter(Client.deleted_at.is_(None)).all()
    return [
        {
            'id': rep.id,
            'name': rep.name,
            'enterprise_id': rep.enterprise_id
        } for rep in clients
    ]
