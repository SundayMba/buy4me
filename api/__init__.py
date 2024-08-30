from flask import Flask
from flasgger import Swagger
from api.v1.routes.main import main as main_blueprint
from api.config import config

swagger = Swagger()

def create_app(env_name):
    """Flask Application factory function
    
    Keyword arguments:
    argument -- config class
    Return: Flask App instance
    """
    app = Flask(__name__)
    app.config.from_object(config.get(env_name))
    swagger.init_app(app)

    """
        Register Application Blueprint Below
    """
    app.register_blueprint(main_blueprint, url_prefix="/api/v1")

    return app