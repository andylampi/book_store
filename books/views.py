from django.views import generic
from .models import Books


class ListViewBook(generic.ListView):
    model = Books
    context_object_name = "book_list"
    template_name = "book/books_list.html"

class DetailViewBook(generic.DetailView):
    model = Books
    context_object_name = "book"
    template_name = "book/books_detail.html"