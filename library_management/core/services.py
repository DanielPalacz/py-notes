from typing import List
from library_management.core.models import Book
from library_management.core.ports import BookRepository

class LibraryService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def add_book(self, title: str, author: str, isbn: str) -> None:
        book = Book(title=title, author=author, isbn=isbn)
        self.book_repository.add_book(book)

    def list_books(self) -> List[Book]:
        return self.book_repository.get_all_books()
