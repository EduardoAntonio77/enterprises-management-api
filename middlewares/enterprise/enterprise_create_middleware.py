from models.enterprise_model import Enterprise
from models.representative_model import Representative

def enterprise_create(data): 
    required_fields = ['name', 'client_quantity', 'address', 'phone', 'representative_id']
    for field in required_fields:
        if field not in data:
            return f"Missing field: {field}"


    duplicate_name = Enterprise.query.filter_by(name=data['name']).first()
    if duplicate_name:
        return f"An enterprise wiht this name already exists."

    duplicate_phone = Enterprise.query.filter_by(phone=data['phone']).first()
    if duplicate_phone:
        return "An enterprise with this phone number already exists."
    
    representative = Representative.query.get(data["representative_id"])
    if not representative:
        return "Representative not found"
    
    return None