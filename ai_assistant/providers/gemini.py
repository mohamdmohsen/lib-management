import os
from google import genai
from .base import AIProvider

import os
from google import genai
from .base import AIProvider


import os
from google import genai
from .base import AIProvider


class GeminiProvider(AIProvider):
    name = "gemini"

    def __init__(self):
        self.client = genai.Client(
            api_key=os.environ.get("GEMINI_API_KEY")
        )

    def summarize(self, title: str, description: str) -> str:
        prompt = (
            "Write a short, engaging 2-sentence summary for this book.\n"
            f"Title: {title}\n"
            f"Description: {description}"
        )

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        return response.text

    def generate_tags(self, title: str, description: str) -> str:
        prompt = (
            "Generate 5 to 8 short tags for this book.\n"
            "Return only the tags separated by commas.\n\n"
            f"Title: {title}\n"
            f"Description: {description}"
        )

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        return response.text
    
    def find_similar_books(self, title: str, description: str) -> str:

        prompt = (
        "Suggest 5 characteristics that would make another book similar "
        "to this book. Return only the characteristics separated by commas.\n\n"
        f"Title: {title}\n"
        f"Description: {description}"
    )

        response = self.client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )

        return response.text
    def find_similar_books(self, title: str, description: str) -> str:
        prompt = (
            "Analyze this book and identify 5 characteristics that "
            "describe books similar to it.\n"
            "Return only the characteristics separated by commas.\n\n"
            f"Title: {title}\n"
            f"Description: {description}"
        )

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        return response.text