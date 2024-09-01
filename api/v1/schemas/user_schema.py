# api/schemas/user_schema.py
# DUMMY FILE ----- I WILL STILL EDIT
from marshmallow import Schema, fields

class UserSchema(Schema):
	"""Schema for the User model."""
	id=fields.Int(dump_only=True)
	username=fields.Str(required=True)
	email=fields.Email(required=True)
