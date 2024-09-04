# api/v1/models/user.py

from . import db

class User(db.Model):
	"""
	User model represents a user in the system.
	"""

	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(128), nullable=False)

	def __init__(self, username, email, password):
		"""
		Initialize a new User instance.

		Args:
			username (str): The username of the user.
			email (str): The email address of the user.
			password (str): The password for the user.
		"""
		self.username = username
		self.email = email
		self.password = password

	def __repr__(self):
		"""
		Return a string representation of the User.

		Returns:
			str: String representation.
		"""
		return f'<User {self.username}>'
