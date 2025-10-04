from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from books.models import Book
from .utils import calculate_cart_total
from .models import Order, OrderItem

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

@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    
    if not cart:
        messages.warning(request, 'Your cart is empty!')
        return redirect('cart.index')
    
    book_isbns = list(cart.keys())
    books_in_cart = Book.objects.filter(isbn__in=book_isbns)
    cart_total = calculate_cart_total(cart, books_in_cart)
    
    if request.method == 'POST':
        try:
            # Create the order
            order = Order.objects.create(
                user=request.user,
                total_amount=cart_total
            )
            
            # Create order items
            for book in books_in_cart:
                quantity = int(cart[str(book.isbn)])
                OrderItem.objects.create(
                    order=order,
                    book=book,
                    quantity=quantity,
                    price=book.price
                )
            
            # Clear the cart
            request.session['cart'] = {}
            
            messages.success(request, f'Order #{order.id} has been placed successfully!')
            return redirect('cart.order_success', order_id=order.id)
            
        except Exception as e:
            messages.error(request, 'There was an error processing your order. Please try again.')
            return redirect('cart.index')
    
    template_data = {
        'title': 'Checkout',
        'books_in_cart': books_in_cart,
        'cart_total': cart_total,
        'cart': cart
    }
    
    return render(request, 'cart/checkout.html', {'template_data': template_data})

@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    template_data = {
        'title': 'Order Confirmation',
        'order': order
    }
    return render(request, 'cart/order_success.html', {'template_data': template_data})