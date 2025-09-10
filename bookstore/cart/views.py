from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from books.models import Book
from .utils import  calculate_cart_total

def index(request):
    cart_total = 0
    books_in_cart = []
    cart = request.session.get('cart', {})
    book_isbns = list(cart.keys())
    if (book_isbns != []):
        books_in_cart = Book.objects.filter(isbn__in=book_isbns)
        cart_total = calculate_cart_total(cart, books_in_cart)
    template_data = {}
    template_data['title'] = 'Cart'
    template_data['books_in_cart'] = books_in_cart
    template_data['cart_total'] = cart_total
    return render(request, 'cart/index.html',
        {'template_data': template_data})

def add(request, isbn):
    get_object_or_404(Book, isbn=isbn)
    cart = request.session.get('cart', {})
    cart[isbn] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('cart.index')

def clear(request):
    request.session['cart'] = {}
    return redirect('cart.index')