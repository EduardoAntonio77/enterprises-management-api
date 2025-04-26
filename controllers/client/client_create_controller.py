from config.database import database
from models.client_model import Client

def client_create_controller(data):
    new_client = Client(
        name = data['name'],
        region = data['region'],
        phone = data['phone'],
        cpf = data['cpf'],
        enterprise_id = data['enterprise_id']
    )

    database.session.add(new_client)
    database.session.commit()