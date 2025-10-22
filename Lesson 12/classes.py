from dataclasses import dataclass, field
from typing import Optional, List, Union


# Исключения для валидации
class BookValidationError(Exception):
    pass

class InvalidPageCount(BookValidationError):
    pass

class InvalidYear(BookValidationError):
    pass

class InvalidAuthor(BookValidationError):
    pass

class InvalidPrice(BookValidationError):
    pass


@dataclass(order=True)
class Book:
    pages: int
    year: int
    author: str
    price: float
    book_id: Optional[int] = field(default=None, compare=False)

    def __post_init__(self):
        if not isinstance(self.pages, int) or self.pages <= 0:
            raise InvalidPageCount("Количество страниц должно быть положительным целым числом.")
        if not isinstance(self.year, int) or self.year < 0:
            raise InvalidYear("Год должен быть положительным целым числом.")
        if not isinstance(self.author, str) or not self.author.strip():
            raise InvalidAuthor("Автор должен быть непустой строкой.")
        if not isinstance(self.price, (int, float)) or self.price < 0:
            raise InvalidPrice("Цена должна быть положительным числом.")

    def __str__(self):
        return (f"Книга #{self.book_id if self.book_id is not None else '—'}\n"
                f"Автор: {self.author}\n"
                f"Год: {self.year}, Страниц: {self.pages}\n"
                f"Цена: {self.price:.2f} BYN")


class Library:
    def __init__(self):
        self.books: List[Book] = []
        self._next_id = 1

    def add_book(self, book: Book):
        book.book_id = self._next_id
        self._next_id += 1
        self.books.append(book)

    def get_book_info(self, book_id: int) -> Optional[str]:
        for book in self.books:
            if book.book_id == book_id:
                return str(book)
        return f"Книга с ID {book_id} не найдена."

    def find_by_author(self, author: Union[str, List[str]]) -> List[Book]:
        if isinstance(author, str):
            return [book for book in self.books if book.author == author]
        elif isinstance(author, list):
            return [book for book in self.books if book.author in author]
        else:
            raise TypeError("Автор должен быть строкой или списком строк.")

    def __str__(self):
        return f"Библиотека содержит {len(self.books)} книг."