from config.database import database
from models.product_model import Product

def product_create_controller(data):
    required_fields = ['name', 'price', 'stock', 'enterprise_id']
    for field in required_fields:
        if field not in data:
            return f"Missing field: {field}"

        new_product = Product(
            name=data['name'],
            price=float(data['price']),  
            stock=int(data['stock']),
            enterprise_id=int(data['enterprise_id'])
        )

    database.session.add(new_product)
    database.session.commit()
    return None
