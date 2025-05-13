from config.database import database
from models.product_filters_model import ProductFilters

def product_filter_delete_controller(id):
    product_filter = ProductFilters.query.filter_by(id=id).first()

    database.session.delete(product_filter)
    database.session.commit()