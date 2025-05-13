from config.database import database
from models.product_filters_model import ProductFilters

def create_filter(data):
    new_product_filter = ProductFilters(
        filter_name=data['filter_name'],
        product_id=data['product_id']
    )

    database.session.add(new_product_filter)
    database.session.commit()