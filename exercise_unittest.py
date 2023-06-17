import unittest

def calculate_total_price(items):
    total_price = 0

    for item in items:
        price = item.get('price', 0)
        quantity = item.get('quantity', 0)
            
        try:
            price = float(price)
            quantity = float(quantity)
        
            if( price * quantity > 0): # If price or quantity if negative the sub_total is not included in the total_price
                total_price += price * quantity
        except ValueError as ve:
            print(ve)

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

    def test_multiple_items(self):
        items = [{'name': 'item1', 'price': 10, 'quantity': 2},
                 {'name': 'item2', 'price': 15, 'quantity': 3},
                 {'name': 'item3', 'price': "25", 'quantity': 1}]
        expected_total = 90
        self.assertEqual(calculate_total_price(items), expected_total)

    def test_invalid_price(self):
        items = [{'name': 'item1', 'price': -10, 'quantity': 2}, {'name': 'item1', 'price': "", 'quantity': 2}]
        expected_total = 0  # Negative price should be treated as zero
        self.assertEqual(calculate_total_price(items), expected_total)

    def test_invalid_quantity(self):
        items = [{'name': 'item1', 'price': 10, 'quantity': -2}, 
                 {'name': 'item1', 'price': 10, 'quantity': "value"}, 
                 {'name': 'item1', 'price': 10, 'quantity': 1}]
        expected_total = 10  # Negative quantity should be treated as zero
        self.assertEqual(calculate_total_price(items), expected_total)

if __name__ == '__main__':
    unittest.main()
