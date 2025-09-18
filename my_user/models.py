from django.db import models
# from my_book.models import Book_List
# from my_library.models import library_list
# Create your models here.


class User(models.Model):
    name = models.CharField()
    pers_id = models.IntegerField()
    phone_number = models.IntegerField()
    pers_code = models.IntegerField()
    library = models.ManyToManyField("my_library.library_list",related_name='my_lib',null=True,blank=True)
    book = models.ManyToManyField("my_book.Book_List",related_name='my_book',null=True,blank=True)