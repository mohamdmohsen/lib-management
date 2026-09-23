from django.db import models
from catalog.models import Book


class AIGeneratedContent(models.Model):
    CONTENT_TYPES = (
        ("summary", "Summary"),
        ("similar_books", "Similar Books"),
        ("auto_tags", "Auto Tags"),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="ai_content")
    type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    result = models.TextField()
    provider_used = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('book', 'type')

    def __str__(self):
        return f"{self.book} - {self.type}"