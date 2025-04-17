from database import database 

def client_edit_controller(data, client):

    if 'name' in data:
        client.name = data['name']
    if 'region' in data:
        client.region = data['region']
    if 'phone' in data:
        client.phone = data['phone']
    if 'cpf' in data:
        client.cpf = data['cpf']

    database.session.commit()
