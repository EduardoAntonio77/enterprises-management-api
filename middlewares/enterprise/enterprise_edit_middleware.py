from models.enterprise_model import Enterprise

def enterprise_edit_middleware(id):
    return Enterprise.query.get(id)