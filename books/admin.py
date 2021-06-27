from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    model = Books
    list_display = ("title","author","price")

admin.site.register(Books, BooksAdmin)
