from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Book, Author, Genre, Publisher

User = get_user_model()


class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="TestPassword123!"
        )

        self.author = Author.objects.create(
            name="Test Author"
        )

        self.genre = Genre.objects.create(
            name="Fantasy"
        )

        self.publisher = Publisher.objects.create(
            name="Test Publisher"
        )

        self.book = Book.objects.create(
            title="Test Book",
            isbn="1234567890123",
            description="A test book description",
            publisher=self.publisher
        )

        self.book.author.set([self.author])
        self.book.genres.set([self.genre])

    # --------------------------------
    # GET BOOKS
    # --------------------------------

    def test_get_books(self):
        response = self.client.get(
            "/api/books/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    # --------------------------------
    # CREATE BOOK
    # --------------------------------

    def test_create_book_authenticated(self):
        self.client.force_authenticate(
            user=self.user
        )

        data = {
            "title": "New Book",
            "isbn": "9876543210123",
            "description": "New book description",
            "publisher": self.publisher.id,
            "author": [self.author.id],
            "genres": [self.genre.id],
        }

        response = self.client.post(
            "/api/books/create/",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Book.objects.filter(
                title="New Book"
            ).exists()
        )

    def test_create_book_without_authentication(self):
        data = {
            "title": "Unauthorized Book",
            "isbn": "5555555555555",
            "description": "Should not be created",
            "publisher": self.publisher.id,
            "author": [self.author.id],
            "genres": [self.genre.id],
        }

        response = self.client.post(
            "/api/books/create/",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    # --------------------------------
    # INVALID DATA
    # --------------------------------

    def test_create_book_with_invalid_data(self):
        self.client.force_authenticate(
            user=self.user
        )

        data = {
            "title": "",
            "isbn": "123",
            "description": "",
            "publisher": self.publisher.id,
            "author": [self.author.id],
            "genres": [self.genre.id],
        }

        response = self.client.post(
            "/api/books/create/",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    # --------------------------------
    # FILTERING
    # --------------------------------

    def test_filter_books_by_title(self):
        response = self.client.get(
            "/api/books/?title=Test"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data["count"],
            1
        )

    def test_filter_books_by_author(self):
        response = self.client.get(
            "/api/books/?author=Test Author"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data["count"],
            1
        )

    def test_filter_books_by_genre(self):
        response = self.client.get(
            "/api/books/?genre=Fantasy"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data["count"],
            1
        )

    # --------------------------------
    # RETRIEVE BOOK
    # --------------------------------

    def test_get_single_book(self):
        response = self.client.get(
            f"/api/books/{self.book.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data["title"],
            "Test Book"
        )

    # --------------------------------
    # UPDATE BOOK
    # --------------------------------

    def test_update_book(self):
        self.client.force_authenticate(
            user=self.user
        )

        data = {
            "title": "Updated Book",
            "isbn": self.book.isbn,
            "description": "Updated description",
            "publisher": self.publisher.id,
            "author": [self.author.id],
            "genres": [self.genre.id],
        }

        response = self.client.put(
            f"/api/books/update/{self.book.id}/",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.book.refresh_from_db()

        self.assertEqual(
            self.book.title,
            "Updated Book"
        )

    # --------------------------------
    # DELETE BOOK
    # --------------------------------

    def test_delete_book(self):
        self.client.force_authenticate(
            user=self.user
        )

        response = self.client.delete(
                f"/api/books/delete/{self.book.id}/"
        )

        self.assertIn(
            response.status_code,
            [
                status.HTTP_200_OK,
                status.HTTP_204_NO_CONTENT
            ]
        )

        self.assertFalse(
            Book.objects.filter(
                id=self.book.id
            ).exists()
        )