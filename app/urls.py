from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('all_book/', all_book, name='all_books'),
    path('available_books/', available_books, name='available_books'),
    path('users/', show_users, name='show_users'),
    path('borrowed_books/', show_borrowed_books, name='show_borrowed_books'),
    path('add_user/', add_user, name='add_user'),
    path('add_book/', add_book, name='add_book'),
    path('borrow_book/', borrow_book, name='borrow_book'),
]