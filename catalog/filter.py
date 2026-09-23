from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Book



class BookFilter(filters.FilterSet):

    title = filters.CharFilter(
        field_name="title",
        lookup_expr="icontains"
    )

    author = filters.CharFilter(
        field_name="author__name",
        lookup_expr="icontains"
    )

    genre = filters.CharFilter(
        field_name="genres__name",
        lookup_expr="icontains"
    )

    publisher = filters.CharFilter(
        field_name="publisher__name",
        lookup_expr="icontains"
    )

    class Meta:
        model = Book
        fields = ("title", "author", "genre", "publisher")