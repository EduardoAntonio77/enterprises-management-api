from database import database;
from models.representative_model import Representative;

# controller é tudo q mexe com banco, cutuca o banco
def register_representative_controller(data):
    newrepresentative = Representative(
       name=data['name'],
       cnpj=data['cnpj'],
       email=data['email'],
       phone=data['phone'],
       password=data['password']
    );
    database.session.add(newrepresentative);
    database.session.commit();