# api/v1/models/user_model.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)

	def __init__(self, name, email):
		"""Initialize the User instance"""
		self.name = name
		self.email = email

	def __repr__(self):
		"""String representation of the User object"""
		return f'<User {self.name}>'
