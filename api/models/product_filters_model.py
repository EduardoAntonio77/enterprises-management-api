from config.database import database
from datetime import datetime, timezone

class ProductFilters(database.Model):
    __tablename__ = 'product_filters'
    filter_id = database.Column(database.Integer, primary_key = True, autoincrement = True)
    filter_name = database.Column(database.String(100), nullable = False)
    created_at = database.Column(database.DateTime, default = datetime.now(timezone.utc), nullable = False)
    deleted_at = database.Column(database.DateTime, nullable = True)

    product_id = database.Column(database.Integer, database.ForeignKey('products.id'), nullable = False);
