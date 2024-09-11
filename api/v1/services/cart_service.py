from ..models.cart_order_model import Cart, CartItem, Order, db

class CartService:
	@staticmethod
	def create_cart(user_id):
		"""Create a new cart for a user."""
		cart = Cart(user_id=user_id)
		db.session.add(cart)
		db.session.commit()
		return cart

	@staticmethod
	def add_product_to_cart(cart_id, product_id, quantity):
		"""Add a product to a specific cart."""
		# Fetch cart and product
		cart = Cart.query.get(cart_id)
		product = Product.query.get(product_id)
		
		# Check if cart or product doesn't exist
		if not cart or not product:
			return None, 404  # Cart or product not found
		
		# Add product to cart
		price_at_time = product.new_price
		cart_item = CartItem(
			cart_id=cart_id,
			product_id=product_id,
			quantity=quantity,
			price_at_time=price_at_time
		)
		db.session.add(cart_item)
		db.session.commit()
		return cart_item, 201

	@staticmethod
	def checkout_cart(cart_id):
		"""Checkout a cart and create an order."""
		# Fetch the cart
		cart = Cart.query.get(cart_id)
		
		# Check if the cart exists or if it's already converted
		if not cart or cart.status != 'active':
			return None, 404  # Cart not found or not active
		
		# Calculate the total price of the items in the cart
		total_price = sum(item.price_at_time * item.quantity for item in cart.cart_items)
		
		# Create the order
		order = Order(
			user_id=cart.user_id,
			cart_id=cart.id,
			total_price=total_price
		)
		
		# Mark the cart as converted
		cart.status = 'converted'
		
		# Commit the changes
		db.session.add(order)
		db.session.commit()
		return order, 201