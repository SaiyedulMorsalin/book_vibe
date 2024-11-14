from django.db import models
from categories.models import Category
# Create your models here.
class Book(models.Model):
    image1 = models.ImageField(upload_to='media/book/images',blank=True,null=True)
    image2 = models.ImageField(upload_to='media/book/images',blank=True,null=True)
    image3 = models.ImageField(upload_to='media/book/images',blank=True,null=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=150,null=True,blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    # categories = models.ManyToManyField(to=Category)
    # book_content = models.TextField()
    # description = models.TextField()
    # isbn_number = models.CharField(max_length=13, unique=True)
    # borrow_price = models.PositiveIntegerField()
    # stk_quantity = models.PositiveIntegerField()
    # is_available = models.BooleanField(default=False)
    # discount_price = models.IntegerField(default=50)