from django.urls import path
from . import views

urlpatterns = [
    path("book/list/", views.book_list, name="book_list"),
    path("book/<int:pk>", views.book_detail, name="book_detail"),
    path("book/<int:pk>/edit/", views.book_edit, name="book_edit"),
    path("book/new/", views.book_new, name="book_new"),
    path("author/list/", views.author_list, name="author_list"),
    path("author/<int:pk>", views.author_detail, name="author_detail"),
    path("author/<int:pk>/edit/", views.author_edit, name="author_edit"),
    path("author/new/", views.author_new, name="author_new")
]