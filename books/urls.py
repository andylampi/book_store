from django.urls import path 
from .views import ListViewBook, DetailViewBook

urlpatterns = [ 
    path("", ListViewBook.as_view(), name="book_list"),
    path("<uuid:pk>/", DetailViewBook.as_view(), name="book_detail")
]