from django.db import models
from django.contrib.auth.models import User


class Accounts(models.Model):
   user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_account')
   balance = models.DecimalField(max_digits=12,decimal_places=2,default=0)
   created_at = models.DateTimeField(auto_now_add=True)
   
   
   
   
class Transactions(models.Model):
   transaction = models.ForeignKey(Accounts,on_delete=models.CASCADE,related_name='transaction')
   created_at = models.DateTimeField(auto_now_add=True)