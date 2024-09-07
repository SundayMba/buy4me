from ..models.product import Product, db

class ProductService:
	@staticmethod
	def create_product(data):
		product = Product(
			name=data['name'],
			category=data['category'],
			image=data.get('image'),
			new_price=data['new_price'],
			old_price=data.get('old_price')
		)
		db.session.add(product)
		db.session.commit()
		return product, 201

	@staticmethod
	def get_all_products():
		return Product.query.all(), 200

	@staticmethod
	def get_product_by_id(product_id):
		product = Product.query.get(product_id)
		if product:
			return product, 200
		else:
			return {"message": "Product not found"}, 404