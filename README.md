# 📚 Library Management API

A backend REST API for managing a digital library, built with **Django** and **Django REST Framework**.

The project includes authentication, book management, filtering, pagination, favorites, reviews, automated testing, and AI-powered features such as book summaries, automatic tags, and similar-book recommendations.

---

## 🚀 Features

### 🔐 Authentication

* User registration
* JWT authentication
* Login
* Access token refresh
* Protected API endpoints

### 📚 Book Management

* Create books
* Retrieve all books
* Retrieve a single book
* Update books
* Delete books
* Authors
* Genres
* Publishers

### 🔎 Search & Filtering

Books can be filtered by:

* Title
* Author
* Genre
* Publisher

### 📄 Pagination

The API supports pagination for book listings.

### ❤️ Favorites

Authenticated users can:

* Add books to favorites
* View favorites
* Manage their own favorites

### ⭐ Reviews

Users can create and manage book reviews.

### 🤖 AI Features

The project integrates Google's Gemini API for:

* AI-generated book summaries
* Automatic book tags
* Similar-book recommendations

AI-generated results are cached in the database to reduce unnecessary API requests where applicable.

### 🧪 Automated Testing

The project includes automated API tests covering:

* Getting books
* Creating books
* Authentication requirements
* Invalid book data
* Filtering
* Retrieving individual books
* Updating books
* Deleting books

Run the tests with:

```bash
python manage.py test catalog
```

---

# 🛠️ Tech Stack

| Technology            | Purpose               |
| --------------------- | --------------------- |
| Python                | Programming language  |
| Django                | Backend framework     |
| Django REST Framework | REST API              |
| SQLite                | Development database  |
| JWT                   | Authentication        |
| django-filter         | API filtering         |
| Google Gemini         | AI features           |
| python-dotenv         | Environment variables |
| Git & GitHub          | Version control       |

---

# 📁 Project Structure

```text
management/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── catalog/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── filters.py
│   ├── pagination.py
│   ├── urls.py
│   └── tests.py
│
├── reviews/
│   └── ...
│
├── ai_assistant/
│   ├── models.py
│   ├── views.py
│   ├── services.py
│   └── providers/
│       ├── base.py
│       └── gemini.py
│
├── manage.py
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/mohamdmohsen/lib-management.git
```

Move into the project:

```bash
cd lib-management
```

---

## 2. Create a virtual environment

Windows:

```bash
python -m venv env
```

Activate it:

```bash
env\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv env
source env/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the same directory as `manage.py`.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True

GEMINI_API_KEY=your-gemini-api-key
```

Do **not** commit `.env` to GitHub.

Your `.gitignore` should contain:

```gitignore
.env
env/
__pycache__/
*.pyc
db.sqlite3
```

---

# 🗄️ Database

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

---

# ▶️ Running the Server

Start the development server:

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

---

# 🔌 API Endpoints

## Authentication

### Register

```http
POST /api/register/
```

### Login

```http
POST /api/token/
```

### Refresh Token

```http
POST /api/token/refresh/
```

---

# 📚 Books

### Get Books

```http
GET /api/books/
```

### Get Single Book

```http
GET /api/books/<id>/
```

### Create Book

```http
POST /api/books/create/
```

Authentication required.

### Update Book

```http
PUT /api/books/update/<id>/
```

Authentication required.

### Delete Book

```http
DELETE /api/books/delete/<id>/
```

Authentication required.

---

# 🔎 Filtering

Examples:

```http
GET /api/books/?title=harry
```

```http
GET /api/books/?author=rowling
```

```http
GET /api/books/?genre=fantasy
```

```http
GET /api/books/?publisher=bloomsbury
```

Filters can also be combined.

Example:

```http
GET /api/books/?title=harry&genre=fantasy
```

---

# 📄 Pagination

The books endpoint supports pagination.

Example:

```http
GET /api/books/?page=2
```

You can also control the page size:

```http
GET /api/books/?page=2&page_size=20
```

The maximum page size is controlled by the API.

---

# ❤️ Favorites

Authenticated users can manage their favorite books through the favorites endpoints.

Users are restricted from modifying other users' favorite records.

---

# ⭐ Reviews

Users can create and manage reviews for books.

Reviews are associated with:

* User
* Book
* Rating
* Comment
* Creation date

---

# 🤖 AI Endpoints

AI functionality requires a valid Gemini API key.

### Generate Book Summary

```http
GET /api/books/<id>/generate-summary/
```

Example response:

```json
{
    "summary": "A short AI-generated summary of the book."
}
```

### Generate Book Tags

```http
GET /api/books/<id>/generate-tags/
```

Example:

```json
{
    "tags": "Fantasy, Adventure, Magic, Mystery, Young Adult"
}
```

### Find Similar Books

```http
GET /api/books/<id>/generate-similar-books/
```

The API analyzes the selected book and compares it against available books to identify similar titles.

---

# 🧪 Testing

Run all catalog tests:

```bash
python manage.py test catalog
```

Django automatically creates a temporary test database, runs the tests, and destroys the test database afterward.

---

# 🔐 Authentication Example

After obtaining a JWT access token:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Protected endpoints require authentication.

---

# 🧠 Architecture

The project separates AI functionality from the main catalog application.

```text
Client
   │
   ▼
Django REST API
   │
   ├── Accounts
   │      └── JWT Authentication
   │
   ├── Catalog
   │      ├── Books
   │      ├── Authors
   │      ├── Genres
   │      └── Publishers
   │
   ├── Reviews
   │
   ├── Favorites
   │
   └── AI Assistant
          │
          ▼
      AI Provider
          │
          ▼
        Gemini
```

The AI provider layer is designed so that AI functionality can be separated from the rest of the application and additional providers can be added later.

---

# 🔮 Future Improvements

Planned improvements include:

* [ ] PostgreSQL
* [ ] Docker
* [ ] API documentation with Swagger/OpenAPI
* [ ] Production deployment
* [ ] GitHub Actions / CI
* [ ] React frontend
* [ ] Improved AI caching
* [ ] More comprehensive automated tests
* [ ] Production security configuration

---

# 👨‍💻 Author

**Mohamed Mohssen**

Backend / Software Engineering project built with Django REST Framework.

---

## 📄 License

This project is for educational and portfolio purposes.
