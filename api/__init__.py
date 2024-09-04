# api/__init__.py

from flask import Flask
from api.v1.models import db
from api.config import config

def create_app(config_name):
    """
    Create and configure the app.
    
    Args:
 	   config_name (str): The configuration name to use.
    
    Returns:
 	   Flask: The configured Flask app.
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)

    with app.app_context():
 	   # Import the routes here to register them with the app
 	   from api.v1.routes.main import main as main_blueprint
 	   app.register_blueprint(main_blueprint)

    return app
