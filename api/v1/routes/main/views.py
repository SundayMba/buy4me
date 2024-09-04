# api/v1/routes/main/views.py

from flask import request, jsonify
from api.v1.routes.main import main
from api.v1.schemas import user_schema, users_schema
from api.v1.services import (
	create_user,
	get_user_by_id,
	get_all_users,
	update_user,
	delete_user
)

@main.route('/users', methods=['POST'])
def add_user():
	"""
	Add a new user.
	---
	parameters:
	  - name: body
		in: body
		required: true
		schema:
		  id: User
		  required:
			- username
			- email
			- password
		  properties:
			username:
			  type: string
			email:
			  type: string
			password:
			  type: string
	responses:
	  201:
		description: User created successfully.
	  400:
		description: Invalid input.
	"""
	data = request.get_json()
	if not data:
		return jsonify({"message": "No input data provided"}), 400

	try:
		user = create_user(
			username=data['username'],
			email=data['email'],
			password=data['password']
		)
		result = user_schema.dump(user)
		return jsonify(result), 201
	except Exception as e:
		return jsonify({"message": str(e)}), 400

@main.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
	"""
	Get a user by ID.
	---
	parameters:
	  - name: user_id
		in: path
		type: integer
		required: true
		description: The ID of the user.
	responses:
	  200:
		description: A single user.
	  404:
		description: User not found.
	"""
	user = get_user_by_id(user_id)
	if not user:
		return jsonify({"message": "User not found"}), 404

	result = user_schema.dump(user)
	return jsonify(result), 200

@main.route('/users', methods=['GET'])
def get_users():
	"""
	Get all users.
	---
	responses:
	  200:
		description: A list of users.
	"""
	users = get_all_users()
	result = users_schema.dump(users)
	return jsonify(result), 200

@main.route('/users/<int:user_id>', methods=['PUT'])
def update_existing_user(user_id):
	"""
	Update a user's information.
	---
	parameters:
	  - name: user_id
		in: path
		type: integer
		required: true
		description: The ID of the user.
	  - name: body
		in: body
		required: true
		schema:
		  id: UserUpdate
		  properties:
			username:
			  type: string
			email:
			  type: string
			password:
			  type: string
	responses:
	  200:
		description: User updated successfully.
	  400:
		description: Invalid input.
	  404:
		description: User not found.
	"""
	data = request.get_json()
	if not data:
		return jsonify({"message": "No input data provided"}), 400

	user = update_user(user_id, data)
	if not user:
		return jsonify({"message": "User not found"}), 404

	result = user_schema.dump(user)
	return jsonify(result), 200

@main.route('/users/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
	"""
	Delete a user.
	---
	parameters:
	  - name: user_id
		in: path
		type: integer
		required: true
		description: The ID of the user.
	responses:
	  200:
		description: User deleted successfully.
	  404:
		description: User not found.
	"""
	success = delete_user(user_id)
	if not success:
		return jsonify({"message": "User not found"}), 404

	return jsonify({"message": "User deleted successfully"}), 200
