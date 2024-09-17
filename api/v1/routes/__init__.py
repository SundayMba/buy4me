from flask import Blueprint

main_bp = Blueprint("main", __name__)
auth_bp = Blueprint("auth", __name__)
error_bp = Blueprint("error", __name__)
photo_bp = Blueprint("photo", __name__)

from . import main, errors, auth, photo
