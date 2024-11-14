from django.shortcuts import render
from book.models import Book
# Create your views here.
def home_page(request):
    books = Book.objects.all()
    print(books)
    return render(request,'index.html',{'books':books})

