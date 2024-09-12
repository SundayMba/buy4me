from flask import Blueprint, request, jsonify
from ..services.order_service import OrderService
from ..schemas.order_schema import OrderSchema
from flasgger.utils import swag_from

order_bp = Blueprint('order', __name__)

@order_bp.route("/orders/<int:user_id>", methods=["GET"])
@swag_from("./documentation/cart_order.yml")
def get_orders(user_id):
	"""Get all orders for a user"""
	orders = OrderService.get_orders_by_user(user_id)
	return jsonify(OrderSchema(many=True).dump(orders)), 200
