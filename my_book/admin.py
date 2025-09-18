from django.contrib import admin
from .models import Category,Book_List
# Register your models here.

class Category_Admin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['title']

class Book_List_Admin(admin.ModelAdmin):
    list_display = ['category','name','auther','book_code','amount','status']
    search_fields = ['category','name','auther','book_code','library__lib_code','user__pers_code','wait_list__pers_code']
    list_filter = ['category','name','auther','book_code','library__lib_code','user__pers_code','wait_list__pers_code']

admin.site.register(Category,Category_Admin)
admin.site.register(Book_List,Book_List_Admin)