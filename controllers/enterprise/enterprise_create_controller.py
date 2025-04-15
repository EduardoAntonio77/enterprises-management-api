# Imports
from database import database
from models.enterprise_model import Enterprise

def create_enterprise(data):
    new_enterprise = Enterprise(
        name=data['name'],
        client_quantity=data["client_quantity"],
        address=data['address'],
        phone=data['phone'],
        representative_id=["representative_id"]
    )

    database.session.add(new_enterprise)
    database.session.commit()