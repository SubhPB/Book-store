#  Byimaan

from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    
    path('', BookListView.as_view(), name='book_list'),

    # for individual book
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail')
]