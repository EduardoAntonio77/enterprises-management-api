# imports
from config.database import database;
from datetime import timezone, datetime;

# clients model
class Client(database.Model):
    __tablename__ = "clients";
    id = database.Column(database.Integer, primary_key = True, autoincrement = True);
    name = database.Column(database.String(200), nullable = False);
    region = database.Column(database.String(100), nullable = False);
    phone = database.Column(database.String(50), nullable = False, unique = True);
    cpf = database.Column(database.String(50), nullable = False, unique = True);
    created_at = database.Column(database.DateTime, nullable = False, default = datetime.now(timezone.utc));
    deleted_at = database.Column(database.DateTime, nullable = True);

    enterprise_id = database.Column(database.Integer, database.ForeignKey('enterprise.id'), nullable = False);