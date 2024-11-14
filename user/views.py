from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from .import forms 
from .models import BorrowBook
from book.models import Book





# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = forms.UserLoginForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            print("Username:", user_name)
            print("Password:", user_pass)
            
            user = authenticate(request, username=user_name, password=user_pass)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse_lazy("home_page"))
            else:
                print("Authentication failed.")
                messages.error(request, "Please provide the correct login information.")
                return redirect('user_login')
        else:
            print("Form errors:", form.errors)
            messages.error(request, "Please provide the correct login information.")
    else:
        form = forms.UserLoginForm()
    
    return render(request, 'login.html', {'form': form})

    
    
    
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('user_login')
    
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form' : register_form, 'type' : 'Register'})


def user_logout(request):
    logout(request)
    return redirect('home_page')

@login_required(login_url="user_login")
def user_profile(request, name):

    user = request.user

    borrow_books = BorrowBook.objects.filter(user=user)

    return render(
        request,
        "user_profile.html",
        {"all_borrow": borrow_books,},
    )
    
    
    
@login_required(login_url="user_login")
def user_profile_edit(request):
    return render(request,'user_profile_edit.html')


@login_required(login_url="user_login")
def return_pay( request, id):
    borrow_book = get_object_or_404(BorrowBook, id=id)
    
    try:
        borrow_book.delete()
        messages.success(request, f"You have successfully returned '{borrow_book.book.title}'.")
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
    
    return redirect("user_profile", request.user.username)


try:

    @login_required(login_url="user_login")
    def borrow_now(request, book_title, book_id):
        book = get_object_or_404(Book, id=book_id)
        

        if request.user is None:
            return redirect("user_login")

        borrow = BorrowBook.objects.create(
            user=request.user,
            book=book,
            quantity=1,
            total_price=book.price,
        )
        if borrow:
            book.save()
    

            messages.success(
                request,
                f'Successfully Purchase {"{:,.2f}".format(float(book.price))}$ from your account',
            )
            return redirect("borrow_conf", book_id=borrow.id)
        else:
            messages.error(
                request,
                "Can't Borrow this book.",
            )
            return redirect("book_detail", book.title, book.id)

    def borrow_confirmation(request, book_id):
        borrow = get_object_or_404(BorrowBook, id=book_id, user=request.user)
        return render(request, "borrow_conf.html", {"borrow": borrow})

except Exception as e:
    print(e)