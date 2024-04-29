# Byimaan

from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Book

# at /books/
class BookListView(LoginRequiredMixin, ListView):
    # ListView will allow us to access model.objects in html with the default name of 'object_list' 
    model = Book

    # To change the default name from 'object_list'
    context_object_name = 'books'

    # the html file 's address where 'book_list' will be available
    template_name = 'books/book_list.html'
    login_url = 'account_login'


# at /books/<int:pk>
class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book

    # changing default name of 'object' to book
    context_object_name = 'book'    
    template_name = 'books/book_detail.html'
    login_url='account_login'

    # custom permission
    permission_required = 'books.special_status'

class SearchResultsListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name='books'
    template_name='books/book_list.html'
    login_url='account_login'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=q) | Q(title__icontains=q)
        )