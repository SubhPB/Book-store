# Byimaan

from django.test import TestCase
from django.urls import reverse
from .models import Book

class BoookTests(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title='Game of Thrones IX',
            author= 'R. R. George Martin',
            price='25.00'
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Game of Thrones IX')
        self.assertEqual(f'{self.book.author}', 'R. R. George Martin')
        self.assertEqual(f'{self.book.price}', '25.00')

    def test_book_list(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Game of Thrones IX')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('books/1234/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Game of Thrones IX')
        self.assertTemplateUsed(response, 'books/book_detail.html')