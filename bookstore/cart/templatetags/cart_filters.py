from django import template
register = template.Library()

@register.filter(name='get_quantity')
def get_cart_quantity(cart, book_isbn):
    return cart[str(book_isbn)]

@register.filter(name='calculate_subtotal')
def calculate_subtotal(book, cart):
    quantity = int(cart[str(book.isbn)])
    return book.price * quantity