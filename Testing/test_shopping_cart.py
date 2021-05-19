import io

from unittest import mock

from shopping_cart import add_sales_tax, ShoppingCart
from product import Product


class TestShoppingCart:
	def test_add_and_remove_product(self):
		cart = ShoppingCart()
		product = Product('shoes', 'S', 'blue')
		cart.add_product(product)

		assert {'SHOES-S-BLUE': {'quantity': 1}} == cart.products

		cart.remove_product(product)
		assert {} == cart.products
		
		for i in range(5):
			cart.remove_product(product)
			
		assert {} == cart.products

	def test_remove_nonexisting_products(self):
		cart = ShoppingCart()
		product = Product('shoes', 'S', 'blue')

		for i in range(5):
			cart.remove_product(product)

		assert {} == cart.products

	@mock.patch('shopping_cart.urlopen')
	def test_get_sales_tax_returns_proper_value_from_api(self, mock_urlopen):
		test_tax_rate = 1.06
		mock_urlopen.return_value = io.BytesIO(str(test_tax_rate).encode('utf-8'))
		assert 5 * test_tax_rate == add_sales_tax(5, 'USA', 'MI')
