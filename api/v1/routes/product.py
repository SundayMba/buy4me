from flask import Blueprint, jsonify, request
from flasgger.utils import swag_from
from ..services.product_service import productService
from ..schemas.product_schema import validate_product_input

product_bp = Blueprint('products', __name__)

@product_bp.route("/products", methods=["POST"])
@swag_from('./documentation/product.yml')  # Swagger documentation for creating a product
def create_product():
	"""Create a new product"""
	data = request.json
	errors, status = validate_product_input(data)
	if status == 400:
		return jsonify({
			"message": "Invalid input. Please check your data.",
			"status_code": status,
			"errors": errors
		}), status
	
	product, status_code = productService.create(data)
	return jsonify({
		"message": "Product created successfully",
		"status_code": status_code,
		"data": product.to_dict()
	}), status_code

@product_bp.route("/products", methods=["GET"])
def get_products():
	"""Get all products"""
	products, status_code = productService.fetch_all()
	return jsonify([product.to_dict() for product in products]), status_code

@product_bp.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
	"""Get a product by ID"""
	product, status_code = productService.fetch_by_id(product_id)
	if status_code == 200:
		return jsonify(product.to_dict()), status_code
	else:
		return jsonify(product), status_code