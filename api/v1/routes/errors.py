from flask import jsonify
from . import error_bp




# Custom error handler for 400 Bad Request
@error_bp.app_errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": error.description}), 400

# Custom error handler for 401 Unauthorized
@error_bp.app_errorhandler(401)
def unauthorized(error):
    return jsonify({"error": "Unauthorized", "message": "Authentication is required"}), 401

# Custom error handler for 404 Not Found
@error_bp.app_errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "message": "The requested resource was not found"}), 404