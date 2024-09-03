# api/v1/models/__init__.py

from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy instance
db = SQLAlchemy()

# Import models so they are registered with SQLAlchemy
from .user import User
