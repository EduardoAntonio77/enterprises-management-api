from models.product_model import Product
from models.enterprise_model import Enterprise

def product_create(data):
    required_fields = ['name', 'price', 'stock']
    for field in required_fields:
        if field not in data:
            return f"Missing field: {field}"
    
    enterprise = Enterprise.query.filter_by(id=data['enterprise_id']).first()

    if not enterprise:
        return "Enterprise not found"
    
    return None