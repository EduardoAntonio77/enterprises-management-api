from config.database import database
from models.product_model import Product

def product_delete_controller(id):
    product = Product.query.filter_by(id=id).first()
    
    database.session.delete(product)
    database.session.commit()