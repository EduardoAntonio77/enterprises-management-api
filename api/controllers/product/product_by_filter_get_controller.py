from flask import jsonify
from models.product_model import Product
from models.product_filters_model import ProductFilters
from config.database import database
from sqlalchemy import func, case

def get_products_by_filters_controller(ids):
    if not ids or not isinstance(ids, list):
        return jsonify({'error': 'O parâmetro "ids" é obrigatório e deve ser uma lista'}), 400

    query = (
        database.session.query(Product.id)
        .join(Product.filters)
        .group_by(Product.id)
        .having(func.count(case((ProductFilters.filter_id.in_(ids), 1))) == len(ids))
        .subquery()
    )

    products = Product.query.filter(Product.id.in_(query)).all()

    if not products:
        return jsonify({
            "status": 404,
            "message": f"No products found with the following filters: {ids}"
        }), 404

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