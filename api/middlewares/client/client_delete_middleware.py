from models.client_model import Client

def validate_client_exists(id):
    client = Client.query.get(id)
    if not client or client.deleted_at:
        return "Client not found or already deleted"

    return None

    