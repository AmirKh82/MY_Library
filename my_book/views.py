from django.shortcuts import render
from .models import Book_List
from django.http.response import JsonResponse , HttpResponse
from my_user.models import User
# Create your views here.



def show_all_book(request):
    books = Book_List.objects.all().values()
    book = list(books)
    return JsonResponse(book,safe=False)



def reserve_book(request,book_code,pers_code):
    try:
        book = Book_List.objects.get(book_code=book_code)
        user = User.objects.get(pers_code=pers_code)
    except Book_List.DoesNotExist:
        return HttpResponse("the book not found")
    except User.DoesNotExist:
        return HttpResponse("the user not found")

    if book.amount > 0 :
        book.user.add(user)
        book.amount -= 1
        # book.status = True
        book.status = (book.amount > 0)
        book.save()
        return HttpResponse(f"the book named : '{book.name}' with code : {book.book_code} is reserves for {user.name} with code : {user.pers_code}")
    else :
        book.wait_list.add(user)
        book.status = False
        book.save()
        return HttpResponse(f"the user named : '{user.name}' with code : {user.pers_code} add to wait list for book named : {user.name} with code : {book.book_code}")