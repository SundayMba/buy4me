from marshmallow import Schema, fields, ValidationError

class ProductSchema(Schema):
	name = fields.Str(required=True)
	category = fields.Str(required=True)
	section = fields.Str(required=True, default="product")
	image = fields.Str(required=False)
	new_price = fields.Float(required=True)
	old_price = fields.Float(required=False)

def validate_product_input(data):
	schema = ProductSchema()
	try:
		return schema.load(data), 200
	except ValidationError as err:
		return err.messages, 400