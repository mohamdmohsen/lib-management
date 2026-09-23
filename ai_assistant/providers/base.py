from abc import ABC, abstractmethod


class AIProvider(ABC):
    name = "base"

    @abstractmethod
    def summarize(self, title: str, description: str) -> str:
        pass

    @abstractmethod
    def generate_tags(self, title: str, description: str) -> str:
        pass

    @abstractmethod
    def find_similar_books(self, title: str, description: str) -> str:
        pass