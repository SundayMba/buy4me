# api/v1/services/user_service.py

from api.v1.models import db, User

def create_user(username, email, password):
	"""
	Create a new user and add to the database.

	Args:
		username (str): The username of the user.
		email (str): The email address of the user.
		password (str): The password for the user.

	Returns:
		User: The created User object.
	"""
	new_user = User(username=username, email=email, password=password)
	db.session.add(new_user)
	db.session.commit()
	return new_user

def get_user_by_id(user_id):
	"""
	Retrieve a user by their ID.

	Args:
		user_id (int): The ID of the user.

	Returns:
		User: The User object if found, else None.
	"""
	return User.query.get(user_id)

def get_all_users():
	"""
	Retrieve all users from the database.

	Returns:
		list: List of User objects.
	"""
	return User.query.all()

def update_user(user_id, data):
	"""
	Update a user's information.

	Args:
		user_id (int): The ID of the user to update.
		data (dict): A dictionary of fields to update.

	Returns:
		User: The updated User object.
	"""
	user = User.query.get(user_id)
	if not user:
		return None

	for key, value in data.items():
		setattr(user, key, value)

	db.session.commit()
	return user

def delete_user(user_id):
	"""
	Delete a user from the database.

	Args:
		user_id (int): The ID of the user to delete.

	Returns:
		bool: True if deletion was successful, else False.
	"""
	user = User.query.get(user_id)
	if not user:
		return False

	db.session.delete(user)
	db.session.commit()
	return True
