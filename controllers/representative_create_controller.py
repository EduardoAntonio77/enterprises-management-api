from database import database;

def register_representative_controller(newrepresentative):
    database.session.add(newrepresentative)
    database.session.commit()