from django.contrib import admin
from .models import User
# Register your models here.

class User_Admin(admin.ModelAdmin):
    list_display = ['name','pers_id','pers_code']
    search_fields = ['name','pers_id','pers_code','book__book_code','library__lib_code']
    list_filter = ['name','pers_id','pers_code','book__book_code','library__lib_code']

admin.site.register(User,User_Admin)