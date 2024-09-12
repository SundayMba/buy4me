from marshmallow import Schema, fields

class CartItemSchema(Schema):
	id = fields.Int(dump_only=True)
	cart_id = fields.Int(required=True)
	product_id = fields.Int(required=True)
	quantity = fields.Int(required=True)
	price_at_time = fields.Float(dump_only=True)

class CartSchema(Schema):
	id = fields.Int(dump_only=True)
	user_id = fields.Int(required=True)
	status = fields.Str(dump_only=True)
	created_at = fields.DateTime(dump_only=True)
	updated_at = fields.DateTime(dump_only=True)
	cart_items = fields.List(fields.Nested(CartItemSchema))

class CartAddProductSchema(Schema):
	product_id = fields.Int(required=True)
	quantity = fields.Int(required=True)
