from flask import request, jsonify

def get_products_by_filters_middleware(func):
    def wrapper():
        filters = request.args.get('filters')
        if not filters:
            return jsonify({
                'error': 'The "filters" parameter is mandatory'
                    }), 400
        
        try:
            list(map(int, filters.split(',')))  
        except ValueError:
            return jsonify({
                'error': 'These filters must be integers'
                            }), 400
        
        return func()
    
    return wrapper
