from flask import Flask
from api.extensions import swagger, db, migrate, cors, jwt
from api.v1.routes import main_bp, auth_bp, error_bp, photo_bp
from config import config
from api.v1.models import *
from api.v1.routes.product import product_bp  # Import the product blueprint
# from api.v1.routes.cart_routes import cart_bp  # Import the cart blueprint
# from api.v1.routes.order_routes import order_bp  # Import the order blueprint

def create_app(env_name):
	"""Flask Application factory function
	
	Keyword arguments:
	argument -- config class
	Return: Flask App instance
	"""
	app = Flask(__name__)
	app.config.from_object(config.get(env_name))
	swagger.init_app(app)
	db.init_app(app)
	migrate.init_app(app, db)
	cors.init_app(app)
	jwt.init_app(app)

	"""
		Register Application Blueprint Below
	"""
	prefix: str = "/api/v1"
	app.register_blueprint(photo_bp, url_prefix=prefix)
	app.register_blueprint(main_bp, url_prefix=prefix)
	app.register_blueprint(auth_bp, url_prefix=prefix)
	app.register_blueprint(product_bp, url_prefix=prefix)  # Register the product blueprint
	app.register_blueprint(error_bp)
	# app.register_blueprint(cart_bp, url_prefix=prefix)  # Register the cart blueprint
	# app.register_blueprint(order_bp, url_prefix=prefix)  # Register the order blueprint


	return app