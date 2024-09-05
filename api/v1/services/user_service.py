from .service import Service
from sqlalchemy.exc import IntegrityError, DataError, OperationalError
from api import db
from ..models.user import User
import sqlalchemy as sa
from flask_restful import abort
from api.utils.error_response import error_response

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
    
userService = UserService()