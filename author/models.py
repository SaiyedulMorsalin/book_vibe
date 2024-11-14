from django.db import models
from user.models import Reader

class Author(models.Model):
    author = models.OneToOneField(Reader,on_delete=models.CASCADE,related_name='author')
    bio = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    