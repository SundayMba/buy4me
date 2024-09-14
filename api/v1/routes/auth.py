from . import auth_bp
from flasgger.utils import swag_from
from flask import jsonify, request
from ..services.user_service import userService
from ..models.user import User
from ..schemas.user_schema import validateInput

@auth_bp.route("/register", methods=["POST"])
@swag_from("./documentation/register.yml")
def register():
	"""Registration route"""
	data = request.json
	errors, status = validateInput(data)
	if status == 400:
		return jsonify({
			"message": "invalid input. please check your data.",
			"status_code": status,
			"errors": errors
		}), status
	
	user, status_code = userService.create(**data)
	if status_code == 201:
		return jsonify({
			"message": "registered successfully",
			"status_code": status_code,
			"data": user.to_dict()
		}), status_code
	else:
		return jsonify(user), status_code

@auth_bp.route("/login", methods=["POST"])
@swag_from("./documentation/login.yml")
def login():
	"""Login route"""
	data = request.json
	
	# Input validation (can use similar method as in registration)
	# errors, status = validateInput(data, required_fields=['email', 'password'])
	# if status == 400:
	# 	return jsonify({
	# 		"message": "invalid input. please check your data.",
	# 		"status_code": status,
	# 		"errors": errors
	# 	}), status
	
	# Authenticate user
	user, status_code = userService.authenticate(email=data['email'], password=data['password'])

	
	if status_code == 200:
		return jsonify({
			"message": "logged in successfully",
			"status_code": status_code,
			"data": user.to_dict()  # Assuming you return user data (or token)
		}), status_code
	else:
		return jsonify({
			"message": "Invalid credentials. Please try again.",
			"status_code": status_code
		}), status_code
