from ..models.product import Product
from api import db
from .service import Service

class ProductService(Service):

	def create(self, data):
		product = Product(
			name=data['name'],
			category=data['category'],
			image=data.get('image'),
			new_price=data['new_price'],
			old_price=data.get('old_price'),
			section = data['section']
		)
		db.session.add(product)
		db.session.commit()
		return product, 201

	def fetch_all(self):
		return Product.query.all(), 200

	def fetch_by_id(self, product_id):
		product = Product.query.get(product_id)
		if product:
			return product, 200
		else:
			return {"message": "Product not found"}, 404
		
	def fetch_by_email(self):
		pass

	def delete(self, product_id):
		product, status = self.fetch_by_id(product_id)
		if status == 200:
			db.session.delete(product) # mark a product for deletion
			db.session.commit()	# delete the product finally
			return {"message": "user deleted successfully", "status_code": 200}, 200
		return {"message": f"No product with the id: {product_id} found", "status_code": 404}, 404 

	def update(self, product_id):
		pass
		 
productService = ProductService()