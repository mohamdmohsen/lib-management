from django.urls import path

from .views import generate_summary,generate_tags,generate_similar_books


urlpatterns = [
    path(
        "books/<int:book_id>/generate-summary/",
        generate_summary,
        name="generate-summary"
    ),
    path(
    "books/<int:book_id>/generate-tags/",
    generate_tags,
    name="generate-tags"),
    path(
    "books/<int:book_id>/generate-similar-books/",
    generate_similar_books,
    name="generate-similar-books"
),
]
