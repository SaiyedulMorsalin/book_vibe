
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from user.views import register,user_login,user_logout,borrow_now,borrow_confirmation,user_profile,user_profile_edit,return_pay
from core.views import home_page
from book.views import book_detail
urlpatterns = [
    path('admin/', admin.site.urls),
  
  
  
  
    path('', home_page,name="home_page"),
    path('book/<int:id>/',book_detail,name='book_detail'),
    path("book/<str:book_title>/<int:book_id>/", borrow_now, name="borrow_now"),
    path(
        "borrow/confirmation/<int:book_id>/",
        borrow_confirmation,
        name="borrow_conf",
    ),
    path("return/pay/<int:id>", return_pay, name="return_pay"),
    
    
    
    
    #authentication
    path("<str:name>/profile/", user_profile, name="user_profile"),
     path(
        "<str:name>/profile/edit",user_profile_edit,
        name="edit_user_profile",
    ),
    path('login/',user_login,name='user_login'),
    path('register/',register,name='register'),
    path('logout/',user_logout,name='user_logout'),
]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)
