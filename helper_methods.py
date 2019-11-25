def validate_cart_request(product_id, product_name, quantity, price):
    if product_id != 0 and product_name != None and quantity != 0 and price != 0.0:
        return True
    return False

def get_existing_item(cart, id):
    for item in cart:
        if item['product_id'] == id:
            return item
    return {'product_id': None, 'product_name': None, 'quantity': None, 'price': None}
