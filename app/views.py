from sqlite3 import IntegrityError

from django.shortcuts import render, redirect, HttpResponse
from .models import Books, Users, BorrowedBooks
from django.db.models import Sum

def all_book(request):
    books = Books.objects.all()
    return render(request, 'all_books.html', {'books': books})

def available_books(request):
    available_books = Books.objects.filter(count__gt=0)
    return render(request, 'available_books.html', {'available_books': available_books})

def show_users(request):
    users = Users.objects.all()
    return render(request, 'users.html', {'users': users})

def show_borrowed_books(request):
    borrowed_books = BorrowedBooks.objects.all()
    return render(request, 'borrowed_books.html', {'borrowed_books': borrowed_books})
def home(request):
    total_books = Books.objects.aggregate(total=Sum('count')).get('total', 0)
    total_users = Users.objects.count()
    borrowed_books = BorrowedBooks.objects.count()
    available_books = total_books - borrowed_books

    recent_books = Books.objects.order_by('-id')[:5]  # Last 5 books
    recent_borrowed_books = BorrowedBooks.objects.order_by('-borrow_date')[:5]  # Last 5 borrowed books

    return render(request, 'home.html', {
        'total_books': total_books,
        'available_books': available_books,
        'total_users': total_users,
        'borrowed_books': borrowed_books,
        'recent_books': recent_books,
        'recent_borrowed_books': recent_borrowed_books
    })


def add_user(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        role = request.POST.get('role')

        if firstname and lastname and role:
            Users.objects.create(firstname=firstname, lastname=lastname, role=role)
            return redirect('home')

    users = Users.objects.all()
    return render(request, 'add_user.html', {'users': users})

def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        count = request.POST.get('count')
        cover_url = request.POST.get('cover_url')

        if title and author and count:
            Books.objects.create(title=title, author=author, count=count, cover_url=cover_url)
            return redirect('home')
    books = Books.objects.all()
    return render(request, 'add_book.html', {'books': books})

def borrow_book(request):
    if request.method == "POST":
        user_id = request.POST.get('user')
        book_id = request.POST.get('book')
        borrow_date = request.POST.get('borrow_date')
        return_date = request.POST.get('return_date') or None

        try:
            user = Users.objects.get(id=user_id)
            book = Books.objects.get(id=book_id)
            if book.count == 0:
                return redirect('home')
            book.count -= 1
            BorrowedBooks.objects.create(user=user, book=book, borrow_date=borrow_date, return_date=return_date)
            book.save()
            return redirect('home')
        except (Users.DoesNotExist, Books.DoesNotExist, ):
            return redirect('home')
        except IntegrityError:
            return redirect('home')

    borrowed_books = BorrowedBooks.objects.all()
    books = Books.objects.all()
    users = Users.objects.all()
    return render(
        request,
        'borrow_book.html',
        {'borrowed_books': borrowed_books, 'books': books, 'users': users})