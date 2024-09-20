from api import db
from .base_model import BaseModel

class Product(db.Model):
	__tablename__ = 'products'
	
	id = db.Column(db.Integer, nullable=False, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	category = db.Column(db.String(100), nullable=False)
	section = db.Column(db.String(100), nullable=True)
	image = db.Column(db.String(255), nullable=True)
	new_price = db.Column(db.Float, nullable=True)
	old_price = db.Column(db.Float, nullable=True)

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'category': self.category,
			'image': self.image,
			'new_price': self.new_price,
			'old_price': self.old_price,
			"section": self.section
		}