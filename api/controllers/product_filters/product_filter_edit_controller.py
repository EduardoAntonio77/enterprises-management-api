from config.database import database
from models.product_filters_model import ProductFilters

def product_filter_edit_controller(filter, data):
    if 'filter_name' in data:
        filter.filter_name = data['filter_name']
    if 'product_id' in data:
        filter.product_id = data ['product_id']

    database.session.commit()

    return None