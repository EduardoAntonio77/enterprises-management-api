from flask import jsonify
from functools import wraps

def get_products_by_filters_middleware(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        filter_ids = kwargs.get('filter_ids')

        if not filter_ids:
            return jsonify({'error': 'The "filter_ids" parameter is mandatory'}), 400

        try:
            ids = list(map(int, filter_ids.replace('-', ',').split(',')))
        except ValueError:
            return jsonify({'error': 'The filters must be integers'}), 400

        # Passa os IDs processados para o controller via kwargs
        kwargs['ids'] = ids

        return func(*args, **kwargs)

    return wrapper