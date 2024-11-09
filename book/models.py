from django.db import models

# Create your models here.
class Book(models.Model):
    image1 = models.ImageField(upload_to='media/book/images',blank=True,null=True)
    image2 = models.ImageField(upload_to='media/book/images',blank=True,null=True)
    image3 = models.ImageField(upload_to='media/book/images',blank=True,null=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=150,null=True,blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    