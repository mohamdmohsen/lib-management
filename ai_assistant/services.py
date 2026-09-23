from .models import AIGeneratedContent
from .providers.gemini import GeminiProvider
from catalog.models import Book

PROVIDERS = [
    GeminiProvider()
]


def get_book_summary(book):

    cached = AIGeneratedContent.objects.filter(
        book=book,
        type="summary"
    ).first()

    if cached:
        return cached.result

    for provider in PROVIDERS:

        try:
            result = provider.summarize(
                book.title,
                book.description
            )

            AIGeneratedContent.objects.create(
                book=book,
                type="summary",
                result=result,
                provider_used=provider.name
            )

            return result

        except Exception as e:
            print(f"{provider.name} failed: {type(e).__name__}: {e}")
            raise
    raise Exception("All AI providers failed")

def get_book_tags(book):

    cached = AIGeneratedContent.objects.filter(
        book=book,
        type="auto_tags"
    ).first()

    if cached:
        return cached.result

    for provider in PROVIDERS:
        try:
            result = provider.generate_tags(
                book.title,
                book.description
            )

            AIGeneratedContent.objects.create(
                book=book,
                type="auto_tags",
                result=result,
                provider_used=provider.name
            )

            return result

        except Exception as e:
            print(
                f"{provider.name} failed: "
                f"{type(e).__name__}: {e}"
            )
            raise

    raise Exception("All AI providers failed")
def get_similar_books(book):

    cached = AIGeneratedContent.objects.filter(
        book=book,
        type="similar_books"
    ).first()

    books = list(
        Book.objects
        .exclude(id=book.id)
        .prefetch_related("author", "genres")
    )

    if not books:
        return []

    candidate_text = []

    for candidate in books:
        authors = ", ".join(
            author.name for author in candidate.author.all()
        )

        genres = ", ".join(
            genre.name for genre in candidate.genres.all()
        )

        candidate_text.append(
            f"ID: {candidate.id}\n"
            f"Title: {candidate.title}\n"
            f"Description: {candidate.description}\n"
            f"Authors: {authors}\n"
            f"Genres: {genres}\n"
        )

    candidates = "\n".join(candidate_text)

    for provider in PROVIDERS:
        try:
            prompt = (
                "Find the 5 books most similar to the target book "
                "from the candidate books below.\n"
                "Return ONLY the IDs of the similar books separated "
                "by commas.\n\n"

                f"TARGET BOOK:\n"
                f"Title: {book.title}\n"
                f"Description: {book.description}\n\n"

                f"CANDIDATE BOOKS:\n"
                f"{candidates}"
            )

            result = provider.client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt,
            )

            response = result.text

            ids = []

            for value in response.split(","):
                value = value.strip()

                if value.isdigit():
                    ids.append(int(value))

            valid_ids = [
                book_id
                for book_id in ids
                if any(candidate.id == book_id for candidate in books)
            ][:5]

            return [
                candidate
                for candidate in books
                if candidate.id in valid_ids
            ]

        except Exception as e:
            print(
                f"{provider.name} failed: "
                f"{type(e).__name__}: {e}"
            )
            raise

    raise Exception("All AI providers failed")