# Byimaan

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

# at /books/
class BookListView(ListView):
    # ListView will allow us to access model.objects in html with the default name of 'object_list' 
    model = Book

    # To change the default name from 'object_list'
    context_object_name = 'books'

    # the html file 's address where 'book_list' will be available
    template_name = 'books/book_list.html'


# at /books/<int:pk>
class BookDetailView(DetailView):
    model = Book

    # changing default name of 'object' to book
    context_object_name = 'book'    
    template_name = 'books/book_detail.html'