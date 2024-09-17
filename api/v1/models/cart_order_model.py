# from datetime import datetime
# from api import db

# class Cart(db.Model):
# 	__tablename__ = 'carts'
# 	id = db.Column(db.Integer, primary_key=True)
# 	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
# 	status = db.Column(db.String(20), default='active')  # Cart statuses: active, converted
# 	created_at = db.Column(db.DateTime, default=datetime.utcnow)
# 	updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
	
# 	# One cart has many cart items
# 	cart_items = db.relationship('CartItem', backref='cart', lazy=True, cascade="all, delete-orphan")
# 	# A cart may be associated with one order once checked out
# 	order = db.relationship('Order', backref='cart', uselist=False, lazy='joined')

# class CartItem(db.Model):
# 	__tablename__ = 'cart_items'
# 	id = db.Column(db.Integer, primary_key=True)
# 	cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
# 	product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
# 	quantity = db.Column(db.Integer, nullable=False)
# 	price_at_time = db.Column(db.Float, nullable=False)  # Price when the product was added to the cart

# class Order(db.Model):
# 	__tablename__ = 'orders'
# 	id = db.Column(db.Integer, primary_key=True)
# 	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
# 	cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
# 	status = db.Column(db.String(20), default='pending')  # Order statuses: pending, completed, cancelled
# 	total_price = db.Column(db.Float, nullable=False)
# 	created_at = db.Column(db.DateTime, default=datetime.utcnow)
