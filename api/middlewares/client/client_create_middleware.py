from models.client_model import Client
from models.enterprise_model import Enterprise

def client_create(data):
    required_fields = ['name', 'region', 'phone', 'cpf']
    for field in required_fields:
        if field not in data:
            return f"Missing field: {field}"
        
    duplicated_phone = Client.query.filter_by(phone = data['phone']).first()
    if duplicated_phone:
        return "An client with this phone number already exists."
    
    duplicated_cpf = Client.query.filter_by(cpf = data['phone']).first()
    if duplicated_cpf:
        return "An client with this cpf already exists."
    
    enterprise = Enterprise.query.filter_by(id=data['enterprise_id']).first()

    if not enterprise:
        return "Enterprise not found"
    
    return None
