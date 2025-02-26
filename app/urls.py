from django.urls import path
from .views import home, add_user, add_book, borrow_book, all_book

urlpatterns = [
    path('', home, name='home'),
    path('all_book', all_book, name='all_books'),
    path('add_user/', add_user, name='add_user'),
    path('add_book/', add_book, name='add_book'),
    path('borrow_book/', borrow_book, name='borrow_book'),
]