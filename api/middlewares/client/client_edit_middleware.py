from models.client_model import Client

def client_edit_middleware(id):
    return Client.query.get(id)