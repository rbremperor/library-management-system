from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    count = models.PositiveIntegerField(default=1)
    cover_url = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.title


class Users(models.Model):
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
    ]

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Student')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class BorrowedBooks(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='books')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='users')
    borrow_date = models.DateField(auto_now_add=True)  # Set borrow date automatically
    return_date = models.DateField(null=True, blank=True)  # Optional return date
    is_returned = models.BooleanField(default=False)  # Track return status


    class Meta:
        db_table = 'borrowed_books'

    def __str__(self):
        return f"{self.book.title} borrowed by {self.user.firstname}"
