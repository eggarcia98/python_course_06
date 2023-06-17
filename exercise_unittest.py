def calculate_total_price(items):
    total_price = 0
    for item in items:
        price = item.get('price', 0)
        quantity = item.get('quantity', 0)
        total_price += price * quantity
    return total_price