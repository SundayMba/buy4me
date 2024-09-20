from . import auth_bp
from flasgger.utils import swag_from
from flask import jsonify, request
from ..services.user_service import userService, admin_required
from ..models.user import User
from ..schemas.user_schema import validateLogin, validateRegister
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

@auth_bp.route("/register", methods=["POST"])
@swag_from("./documentation/register.yml")
def register():
	"""Registration route"""
	data = request.json
	errors, status = validateRegister(data)
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
	errors, status = validateLogin(data)
	if status == 400:
		return jsonify({
			"message": "invalid input. please check your data.",
			"status_code": status,
			"errors": errors
		}), status
	
	# Authenticate user
	user, status_code = userService.authenticate(email=data['email'], password=data['password'])
	if status_code == 401:
		return jsonify(user), 401
	identity = {
		'user_id': user.id,
		'role': user.role
	}

	# create an access token
	token = create_access_token(identity=identity)
	return jsonify({
		"message": "user logged in successfully",
		"status_code": status_code,
		"token": token,
		"user": identity
	})

@auth_bp.route("/dashboard", methods=["GET"])
@jwt_required()
@admin_required
def admin_dashboard():
	"""Only admins can access this route"""
	current_user = get_jwt_identity()
	return jsonify({
		"message": "welcome to admin dashboard",
		"user": current_user,
		"status_code": 200
	}), 200