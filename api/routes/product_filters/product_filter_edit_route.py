from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required


from middlewares.product_filters.product_filter_edit_middleware import product_filter_edit
from controllers.product_filters.product_filter_edit_controller import product_filter_edit_controller

from flasgger.utils import swag_from

product_filter_edit_blueprint = Blueprint('product_filter_edit_blueprint', __name__)

@product_filter_edit_blueprint.route("/product_filter/<int:filter_id>", methods=['PUT'])
@jwt_required()
@swag_from("../../../docs/product_filter_docs/product_filter_edit_docs.yaml")
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