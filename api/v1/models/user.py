from .base_model import BaseModel
import sqlalchemy as sa
import sqlalchemy.orm as so
from typing import Optional
from api import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, BaseModel):
    __tablename__ = "users"
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(128), index=True, unique=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))
    role: so.Mapped[str] = so.mapped_column(sa.String(20), default=lambda: "user")

    def __init__(self, **kwargs):
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")
        self.role = kwargs.get("role", "user")

    @property
    def password(self):
        """retrieve user  hash password"""
        pass
    
    @password.setter
    def password(self, plain_password):
        """set user hash password"""
        self.password_hash = generate_password_hash(plain_password)

    def verify_password(self, plain_password):
        return check_password_hash(self.password_hash, plain_password)
    
    def to_dict(self):
        """returns a dictionary representation of the instance"""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "role": self.role
        }
