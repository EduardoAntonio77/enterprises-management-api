# controllers/product_controller.py
from flask import request, jsonify
from models.product_model import Product
from models.product_filters_model import ProductFilters
from config.database import database
from sqlalchemy import func, case

def get_products_by_filters_controller():

    filters = request.args.get('filters')
    if not filters:
        return jsonify({'error': 'Parâmetro "filters" é obrigatório'}), 400

    try:
        ids = list(map(int, filters.split(',')))
    except ValueError:
        return jsonify({'error': 'Os filtros devem ser números inteiros'}), 400


    query = (
        database.session.query(Product.id)
        .join(Product.filters)
        .group_by(Product.id)
        .having(func.count(case((ProductFilters.filter_id.in_(ids), 1))) == len(ids))
        .subquery()
    )

    products = Product.query.filter(Product.id.in_(query)).all()

    return jsonify([
        {
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'stock': p.stock,
            'enterprise_id': p.enterprise_id,
            'filters': [f.filter_name for f in p.filters]
        } for p in products
    ])
