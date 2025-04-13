# imports
from database import database;
from datetime import timezone, datetime;

# products model
class Product(database.Model):
    __tablename__ = 'products';
    id = database.Column(database.Integer, primary_key = True, autoincrement = True);
    name = database.Column(database.String(100), nullable = False);
    price = database.Column(database.Integer, nullable = False);
    stock = database.Column(database.Integer, nullable = False);
    created_at = database.Column(database.DateTime, nullable = False, default = datetime.now(timezone.utc));
    deleted_at = database.Column(database.DateTime, nullable = True);

    enterprise_id = database.Column(database.Integer, database.ForeignKey('enterprise.id'), nullable = False);