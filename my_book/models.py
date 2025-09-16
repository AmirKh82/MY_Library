from django.db import models
from my_library.models import library_list
from my_user.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField()

class Book_List(models.Model):
    library = models.ManyToManyField(library_list,on_delete=models.PROTECT,related_name='lib')
    user = models.ManyToManyField(User,on_delete=models.PROTECT,related_name='user')
    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name='category')
    name = models.CharField(max_length=20)
    auther = models.CharField(max_length=20)
    amount = models.IntegerField()
    book_code = models.IntegerField()
    status = models.BooleanField()