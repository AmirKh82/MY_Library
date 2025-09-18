from django.db import models
# from my_library.models import library_list
from my_user.models import User
# Create your models here.


class Category(models.Model):
    title = models.CharField()

    def __str__(self):
        return self.title


class Book_List(models.Model):
    library = models.ManyToManyField("my_library.library_list",related_name='lib',blank=True)
    user = models.ManyToManyField(User,related_name='my_user',blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    name = models.CharField(max_length=20)
    auther = models.CharField(max_length=20)
    amount = models.IntegerField()
    book_code = models.IntegerField()
    status = models.BooleanField()
    wait_list = models.ManyToManyField(User,related_name='my_user_extra',blank=True,default=None)