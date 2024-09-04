# api/v1/schemas/__init__.py

from .user_schema import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)
