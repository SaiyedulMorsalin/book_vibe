from django.shortcuts import render,get_object_or_404
from .models import Book
# Create your views here.
def book_detail(request,id):
    book = get_object_or_404(Book,id=id)
    print(book)
    return render(request,'book_detail.html',{'book':book})