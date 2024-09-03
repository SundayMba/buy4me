# api/__init__.py

from flask import Flask
from flask_migrate import Migrate
from api.v1.models.user import db  # Import the db instance
from api.config import config
from flasgger import Swagger

swagger = Swagger()

def create_app(env_name):
	"""Flask Application factory function"""
	app = Flask(__name__)
	app.config.from_object(config.get(env_name))
	swagger.init_app(app)
	db.init_app(app)
	migrate = Migrate(app, db)

	"""
	Register Application Blueprint Below
	"""
	from api.v1.routes.main import main as main_blueprint
	app.register_blueprint(main_blueprint, url_prefix="/api/v1")

	return app
