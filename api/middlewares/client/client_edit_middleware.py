from models.client_model import Client
from config.database import database

def client_edit_middleware(id):
    return database.session.get(Client, id)