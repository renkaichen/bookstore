from django import template
register = template.Library()
@register.filter(name='get_quantity')
def get_cart_quantity(cart, book_isbn):
    return cart[str(book_isbn)]