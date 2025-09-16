from django.db import models
from my_book.models import Book_List
from my_user.models import User
# Create your models here.

class library_list(models.Model):
    name = models.CharField()
    lib_code = models.IntegerField()
    city = models.CharField()
    book = models.ManyToManyField(Book_List,on_delete=models.PROTECT,related_name='book')
    user = models.ManyToManyField(User,on_delete=models.PROTECT,related_name='user')