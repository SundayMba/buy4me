# api/services/user_service.py
# DUMMY FILE ------ I WILL ATTEND TO IT LATER ------
from ..models.user_model import User
from .. import db

def create_user(username, email, password_hash):
	"""Create and save a new user."""
	user=User(username=username, email=email, password_hash=password_hash)
	db.session.add(user)
	db.session.commit()
	return user
