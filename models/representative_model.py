# imports
from database import database;
from datetime import timezone, datetime;

# representatives model
class Representative(database.Model):
    __tablename__ = 'representative';
    id = database.Column(database.Integer, primary_key = True, autoincrement = True);
    name = database.Column(database.String(100), nullable = False);
    cnpj = database.Column(database.Integer, nullable = False, unique = True,);
    email = database.Column(database.String(200), nullable = False);
    phone = database.Column(database.String(50), nullable = False, unique = True);
    created_at = database.Column(database.DateTime, default = datetime.now(timezone.utc ), nullable = False);
    delete_at = database.Column(database.DateTime, nullable = True);
    password = database.Column(database.String(100), nullable = False)
    