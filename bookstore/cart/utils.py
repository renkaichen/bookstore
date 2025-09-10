def calculate_cart_total(cart, books_in_cart):
    total = 0
    for book in books_in_cart:
        quantity = cart[str(book.isbn)]
        total += book.price * int(quantity)
    return round(total,2)