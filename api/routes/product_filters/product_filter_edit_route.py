from flask import Blueprint, request, jsonify

from middlewares.product_filters.product_filter_edit_middleware import product_filter_edit

from controllers.product_filters.product_filter_edit_controller import product_filter_edit_controller

from flask_jwt_extended import jwt_required

product_filter_edit_blueprint = Blueprint('product_filter_edit_blueprint', __name__)

@product_filter_edit_blueprint.route("/product_filter/<int:filter_id>", methods=['PUT'])
@jwt_required()
def edit_filter(filter_id):
    data = request.json

    filter = product_filter_edit(data, filter_id)
    if isinstance(filter, str):
        return jsonify({
            "status": 404,
            "error": filter
        })
    
    error = product_filter_edit_controller(filter, data)
    if error:
        return jsonify({
            "status": 400,
            "error": error
        })
    
    return jsonify({
        'status': 200,
        'message': "Filter updated successfully"
    }), 200