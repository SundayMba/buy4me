# api/models/user_model.py
# DUMMY FILE ------ DUMMY FILE
from .. import db

class User(db.Model):
	"""User model for storing user details."""
	__tablename__='users'

	id=db.Column(db.Integer, primary_key=True)
	username=db.Column(db.String(50), unique=True, nullable=False)
	email=db.Column(db.String(100), unique=True, nullable=False)
	password_hash=db.Column(db.String(100), nullable=False)

	def __repr__(self):
		"""Return a string representation of the User."""
		return f'<User {self.username}>'
