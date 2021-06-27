from django.test import TestCase
from .models import Books
from django.urls import reverse 
class TestBook(TestCase):
    def setUp(self):
        self.book = Books.objects.create(
            title = "Test",
            book = "this is a book for you",
            author = "andy lampitelli",
            price = 39.00
        )
    def test_list_book(self):
        template = self.client.get(reverse("book_list"))
        self.assertContains(template, self.book.title)
        self.assertTemplateUsed(template, "book/books_list.html")
        self.assertEqual(template.status_code, 200)
        self.assertContains(template, "Test")

    def test_detail_book(self):
        response  = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("book/1234")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test")
        self.assertContains(response, "this is a book for you")
        self.assertTemplateUsed(response, "book/books_detail.html")

