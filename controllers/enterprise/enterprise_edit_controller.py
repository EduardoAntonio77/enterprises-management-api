# Imports
from database import database 

def enterprise_edit_controller(data, enterprise):

    if 'name' in data:
        enterprise.name = data['name']
    if 'client_quantity' in data:
        enterprise.client_quantity = data['client_quantity']
    if 'address' in data:
        enterprise.address = data['address']
    if 'phone' in data:
        enterprise.phone = data['phone']

    database.session.commit()
