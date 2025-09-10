from django.shortcuts import render
from django.db.models import Q
from .models import Book
books = {
    9781338299144: {
        'name': 'Harry Potter and the Sorcerer\'s Stone', 'price': 10, 'description': 'description', 'isbn': 9781338299144
    },
}
def index(request):
    search_term = request.GET.get('search')
    template_data = {}
    if search_term:
        books = Book.objects.filter(Q(title__icontains=search_term) | Q(author__icontains=search_term))
        template_data['title'] = 'Search'
    else:
        books = Book.objects.all()
        template_data['title'] = 'Books'
    template_data['books'] = books
    return render(request, 'books/index.html', {'template_data': template_data})
def show(request, isbn):
    book = Book.objects.get(isbn=isbn)
    template_data = {}
    template_data['title'] = book.title
    template_data['book'] = book
    return render(request, 'books/show.html', {'template_data': template_data})
