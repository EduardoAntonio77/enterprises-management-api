from config.database import database;

# importando modelos
from .representative_model import Representative;
from .enterprise_model import Enterprise;
from .client_model import Client;
from .product_model import Product;
from .product_filters_model import ProductFilters

# Representative → Enterprises
Representative.enterprises = database.relationship(
    'Enterprise',
    backref='representative',
    lazy=True
)

# Enterprise → Clients
Enterprise.clients = database.relationship(
    'Client',
    backref='enterprise',
    lazy=True
)

# Enterprise → Products
Enterprise.products = database.relationship(
    'Product',
    backref='enterprise',
    lazy=True
)

# Product -> ProductFilters
Product.filters = database.relationship(
    'ProductFilters',
    backref='product',
    lazy=True
)