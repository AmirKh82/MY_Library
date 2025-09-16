from django.db import models
from my_book.models import Book_List
from my_library.models import library_list
# Create your models here.


class User(models.Model):
    name = models.CharField()
    pers_id = models.IntegerField()
    phone_number = models.IntegerField()
    pers_code = models.IntegerField()
    library = models.ManyToManyField(library_list,on_delete=models.PROTECT,related_name='lib')
    book = models.ManyToManyField(Book_List,on_delete=models.PROTECT,related_name='book')