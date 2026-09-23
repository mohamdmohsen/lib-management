from django.urls import path , include
from .views import get_books ,get_book ,create_book,delete_book,update_book
urlpatterns = [
    path('books/',get_books,name='books'),
    path('books/create/',create_book,name='create_book'),
    path('books/<str:id>/',get_book,name='books'),
    path('books/delete/<str:id>/',delete_book,name='delete_books'),
    path('books/update/<str:id>/',update_book,name='update_books'),
    
    
]
