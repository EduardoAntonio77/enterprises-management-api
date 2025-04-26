# imports
from config.database import database;
from datetime import timezone, datetime;

# enterprises model
class Enterprise(database.Model):
    __tablename__ = 'enterprise';
    id = database.Column(database.Integer, primary_key = True, autoincrement = True);
    name = database.Column(database.String(100), nullable = False);
    client_quantity = database.Column(database.Integer, nullable = False);
    address = database.Column(database.String(200), nullable = False);
    phone = database.Column(database.String(50), nullable = False);
    create_at = database.Column(database.DateTime, nullable = False, default = datetime.now (timezone.utc));
    deleted_at = database.Column(database.DateTime, nullable = True);

    representative_id = database.Column(database.Integer, database.ForeignKey('representative.id'), nullable = False);