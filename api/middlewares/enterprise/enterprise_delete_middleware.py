from models.enterprise_model import Enterprise;

def enterprise_delete_middleware(id):
    enterprise = Enterprise.query.get(id);
    if not enterprise:
        return f'Enterprise with id {enterprise} not found'
    
    if enterprise.deleted_at:
        return 'This enterprise has already been deleted'
    

    return None