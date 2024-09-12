from marshmallow import Schema, fields

class OrderSchema(Schema):
	id = fields.Int(dump_only=True)
	user_id = fields.Int(required=True)
	cart_id = fields.Int(required=True)
	status = fields.Str(dump_only=True)
	total_price = fields.Float(dump_only=True)
	created_at = fields.DateTime(dump_only=True)
