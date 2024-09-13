from ..models.cart_order_model import Order, db

class OrderService:
	@staticmethod
	def get_orders_by_user(user_id):
		orders = Order.query.filter_by(user_id=user_id).all()
		return orders
