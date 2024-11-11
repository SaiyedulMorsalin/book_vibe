from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    