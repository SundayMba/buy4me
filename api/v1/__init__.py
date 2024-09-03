# api/v1/__init__.py

from flask import Blueprint

# Create the main blueprint for v1
main = Blueprint('main', __name__)

# Import the views and errors modules to associate with the blueprint
from .routes.main import views, errors
