from .base_model import BaseModel
import sqlalchemy as sa
import sqlalchemy.orm as so
from typing import Optional
from api import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model, BaseModel):
	__tablename__ = "users"
	
	id: so.Mapped[str] = so.mapped_column(sa.String(36), primary_key=True, default=lambda: str(uuid4()))  # UUID for user ID
	username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
	email: so.Mapped[str] = so.mapped_column(sa.String(128), index=True, unique=True)
	password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))
	created_at: so.Mapped[datetime] = so.mapped_column(sa.DateTime, default=datetime.utcnow)
	updated_at: so.Mapped[datetime] = so.mapped_column(sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

	def __init__(self, **kwargs):
		self.username = kwargs.get("username")
		self.email = kwargs.get("email")
		self.password = kwargs.get("password")

	@property
	def password(self):
		"""retrieve hashed password"""
		raise AttributeError("Password is not a readable attribute.")

	@password.setter
	def password(self, plain_password):
		"""set hashed password"""
		self.password_hash = generate_password_hash(plain_password)

	def verify_password(self, plain_password):
		"""verify if password matches hash"""
		return check_password_hash(self.password_hash, plain_password)
	
	def to_dict(self):
		"""returns a dictionary representation of the user instance"""
		return {
			"id": self.id,
			"username": self.username,
			"email": self.email,
			"created_at": self.created_at.isoformat(),
			"updated_at": self.updated_at.isoformat()
		}
