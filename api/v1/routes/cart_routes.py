from flask import Blueprint, request, jsonify
from ..services.cart_service import CartService  # Ensure the path matches your structure
from ..schemas.cart_schema import CartSchema, CartAddProductSchema  # Correct import paths
from flasgger.utils import swag_from  # For documentation integration

cart_bp = Blueprint('cart', __name__)

@cart_bp.route("/cart", methods=["POST"])
@swag_from("./documentation/cart_order.yml")  # Ensure the correct path to YAML
def create_cart():
	"""Handles the creation of a new cart for a user"""
	user_id = request.json.get('user_id')  # Retrieve user_id from request body
	cart = CartService.create_cart(user_id)  # Call service to create a cart
	return jsonify(CartSchema().dump(cart)), 201  # Return serialized cart data with 201 status

@cart_bp.route("/cart/<int:cart_id>/add", methods=["POST"])
def add_product_to_cart(cart_id):
	"""Adds a product to a specific cart"""
	data = request.json  # Retrieve data from request body
	schema = CartAddProductSchema()  # Define schema for input validation
	errors = schema.validate(data)  # Validate incoming data
	if errors:
		return jsonify(errors), 400  # Return validation errors if any
	product_id = data['product_id']  # Get product_id from request data
	quantity = data['quantity']  # Get quantity from request data
	cart_item, status_code = CartService.add_product_to_cart(cart_id, product_id, quantity)  # Call service to add product
	if status_code == 404:
		return jsonify({"message": "Cart or Product not found"}), 404  # Handle not found error
	return jsonify({
		"message": "Product added to cart", 
		"data": CartItemSchema().dump(cart_item)  # Return added product data
	}), status_code

@cart_bp.route("/cart/<int:cart_id>/checkout", methods=["POST"])
def checkout_cart(cart_id):
	"""Handles cart checkout and order creation"""
	order, status_code = CartService.checkout_cart(cart_id)  # Call service to checkout cart
	if status_code == 404:
		return jsonify({"message": "Cart not found or already checked out"}), 404  # Handle not found error
	return jsonify({
		"message": "Order created successfully", 
		"data": OrderSchema().dump(order)  # Return created order data
	}), 201