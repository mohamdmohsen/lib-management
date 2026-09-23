from rest_framework.response import Response
from .serializer import BookSerializer
from .models import Book
from rest_framework.decorators import api_view ,permission_classes
from rest_framework import status,generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .pagination import StandardResultsSetPagination




# Create your views here.


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()

    paginator = StandardResultsSetPagination()
    page = paginator.paginate_queryset(books, request)

    serializer = BookSerializer(page, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['Get'])
def get_book(request,id):

    book =Book.objects.get(id = id)

    serializer = BookSerializer(book,many = False)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes(IsAuthenticated)
def create_book(request):
    
    serializer = BookSerializer(data = request.data)

    if serializer.is_valid():
        data = serializer.validated_data

        book=Book.objects.create(
            
            title = data['title'],
            isbn = data['isbn'],
            description = data['description'],
            publisher = data['publisher'],
        )
        book.author.set(data['author'])
        book.genres.set(data['genres'])
        serializer = BookSerializer(book)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)

 
@api_view(['DELETE'])
@permission_classes(IsAuthenticated)
def delete_book(request,id):
       book =get_object_or_404(Book,id = id)

       
       book.delete()

       return Response({"details":"the book has been deleted"})


@api_view(['PUT'])
@permission_classes(IsAuthenticated)
def update_book(request,id):
    book = get_object_or_404(Book,id = id)
    serializer = BookSerializer(book,data = request.data)   
    if serializer.is_valid():
        data = serializer.validated_data
        book.title  = data['title']
        book.isbn = data['isbn']
        book.description = data['description']
        book.publisher = data['publisher']
        book.save()
        book.author.set(data['author'])
        book.genres.set(data['genres'])
        return Response({"details":"book has been updated"},status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors)                    

