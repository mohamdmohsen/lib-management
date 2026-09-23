
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from .services import get_book_summary, get_book_tags,get_similar_books
from catalog.models import Book

from catalog.serializer import BookSerializer
from .services import get_book_summary


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def generate_summary(request, book_id):

    try:
        book = Book.objects.get(id=book_id)

    except Book.DoesNotExist:
        return Response(
            {"error": "Book not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    summary = get_book_summary(book)

    return Response({
        "summary": summary
    })

@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def generate_tags(request, book_id):

    try:
        book = Book.objects.get(id=book_id)

    except Book.DoesNotExist:
        return Response(
            {"error": "Book not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    tags = get_book_tags(book)

    return Response({
        "tags": tags
    })
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def generate_similar_books(request, book_id):

    try:
        book = Book.objects.get(id=book_id)

    except Book.DoesNotExist:
        return Response(
            {"error": "Book not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    similar_books = get_similar_books(book)

    serializer = BookSerializer(
        similar_books,
        many=True
    )

    return Response({
        "similar_books": serializer.data
    })