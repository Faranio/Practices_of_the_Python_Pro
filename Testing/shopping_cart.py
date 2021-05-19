from collections import defaultdict
from urllib.request import urlopen

class ShoppingCart:
	def __init__(self):
		self.products = defaultdict(lambda: defaultdict(int))

	def add_product(self, product, quantity=1):
		sku = product.generate_sku()
		self.products[sku]['quantity'] += quantity

	def remove_product(self, product, quantity=1):
		sku = product.generate_sku()
		self.products[sku]['quantity'] -= quantity

		if self.products[sku]['quantity'] <= 0:
			del self.products[sku]

def add_sales_tax(original_amount, country, region):
	sales_tax_rate = urlopen(f'https://tax-api.com/{country}/{region}').read().decode()
	return original_amount * float(sales_tax_rate)