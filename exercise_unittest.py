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

  