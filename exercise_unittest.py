import unittest

def calculate_total_price(items):
    total_price = 0
    for item in items:
        price = item.get('price', 0)
        quantity = item.get('quantity', 0)
        total_price += price * quantity
    return total_price

class TestCalculateTotalPrice(unittest.TestCase):

    def test_empty_cart(self):
        items = []
        expected_total = 0
        self.assertEqual(calculate_total_price(items), expected_total)

    def test_single_item(self):
        items = [{'name': 'item1', 'price': 10, 'quantity': 2}]
        expected_total = 20
        self.assertEqual(calculate_total_price(items), expected_total)

 
if __name__ == '__main__':
    unittest.main()
