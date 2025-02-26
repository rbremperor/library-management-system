from django.contrib import admin
from .models import Books, Users, BorrowedBooks

# Register your models here.
admin.site.register(Users)
admin.site.register(Books)
admin.site.register(BorrowedBooks)