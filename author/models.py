from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    author = models.OneToOneField(User,on_delete=models.CASCADE,related_name='author')
    bio = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    