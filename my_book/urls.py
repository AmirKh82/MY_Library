from django.urls import path 
from .views import show_all_book , reserve_book

urlpatterns = [
    path('list-books',show_all_book),
    path('reserve-books/<str:book_code>/<str:pers_code>',reserve_book),
]