from product import Product


class TestProduct:
	def test_transform_name_for_sku(self):
		assert 'SHOES' == Product('shoes', 'S', 'black').transform_name_for_sku()

	def test_transform_color_for_sku(self):
		assert 'BLACK' == Product('shoes', 'S', 'black').transform_color_for_sku()

	def test_generate_sku(self):
		assert 'SHOES-S-BLACK' == Product('shoes', 'S', 'black').generate_sku()
		assert '' == Product('', '', '').generate_sku()
		assert '' == Product('', 'S', 'black').generate_sku()
		assert '' == Product('shoes', '', 'black').generate_sku()
		assert '' == Product('shoes', 'S', '').generate_sku()

	def test_space_containing_name(self):
		assert 'TANKTOP' == Product('tank top', 'M', 'red').transform_name_for_sku()