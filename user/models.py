from django.db import models
from django.contrib.auth.models import User
from book.models import Book
# Create your models here.

class Reader(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='book_reader')
    designation = models.CharField(max_length=50,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=90,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    


class BorrowBook(models.Model):
    user = models.ForeignKey(User, related_name="borrow_user", on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, related_name="user_borrow_book", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    borrow_at = models.DateTimeField(auto_now_add=True)

