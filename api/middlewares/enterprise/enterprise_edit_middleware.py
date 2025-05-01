from config.database import database
from models.enterprise_model import Enterprise

def enterprise_edit_middleware(id):
    return database.session.get(Enterprise, id)
