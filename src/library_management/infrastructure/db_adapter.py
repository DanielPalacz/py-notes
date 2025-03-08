from typing import List
from library_management.core.models import Book
from library_management.core.ports import BookRepository

class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def get_all_books(self) -> List[Book]:
        return self.books
