from marshmallow import Schema, fields, validate, ValidationError
from flask import jsonify

class RegisterSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=4))

def validateInput(data):
    schema = RegisterSchema()
    try:
        valid_data = schema.load(data)
        return valid_data, 200
    except ValidationError as err:
        return err.messages, 400