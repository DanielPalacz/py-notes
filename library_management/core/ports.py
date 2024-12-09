# Interface definitions

from abc import ABC, abstractmethod
from typing import List
from library_management.core.models import Book

class BookRepository(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass

