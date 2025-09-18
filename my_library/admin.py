from django.contrib import admin
from .models import library_list
# Register your models here.

class Library_List_Admin(admin.ModelAdmin):
    list_display = ['name','city','lib_code']
    search_fields = ['name','city','lib_code','book__category','user__pers_code']
    list_filter = ['name','city','lib_code','book__category','user__pers_code']

admin.site.register(library_list,Library_List_Admin)