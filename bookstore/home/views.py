from django.shortcuts import render
from books.models import Book
import random

def index(request):
    template_data = {}
    template_data['title'] = 'ReadNow'
    
    # Get a random book to feature
    books = Book.objects.all()
    if books.exists():
        template_data['featured_book'] = random.choice(books)
    else:
        template_data['featured_book'] = None
    
    return render(request, 'home/index.html', {'template_data': template_data})