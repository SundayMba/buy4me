from .service import Service
from sqlalchemy.exc import IntegrityError, DataError, OperationalError
from api import db
from ..models.user import User
import sqlalchemy as sa
from api.utils.error_response import error_response
from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import jsonify

class UserService(Service):
    def create(self, **user_data):
        """Create a new user"""
        try:   
            user = User(**user_data)
            db.session.add(user)
            db.session.commit()
            return user, 201
        except IntegrityError:
            db.session.rollback()
            return error_response(message="User with this email already exist",
                                  status_code=409), 409
        
    def fetch_by_email(self, email):
        query = sa.select(User).where(User.email == email)
        user = db.session.scalars(query).first()
        return user
        
    def fetch_by_id(self, user_id):
        user = db.session.get(User, user_id)
        return user

    def fetch_all(self):
        query = sa.select(User)
        users = db.session.scalars(query).all()
        return users

    def delete(self):
        pass
    
    def update(self):
        pass

    def authenticate(self, **kwargs):
        email, password = kwargs.values()
        user = self.fetch_by_email(email)
        if user and user.verify_password(password):
            return user, 200
        return {'message': "Invalid email or password", "status": 401}, 401
    
userService = UserService()


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user = get_jwt_identity()
        if user['role'] != 'admin':
            return jsonify({
                "message": "Only admins can access this route.",
                "status_code": 401
            }), 401
        return fn(*args, **kwargs)
    return wrapper
