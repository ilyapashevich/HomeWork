from classes import Book, Library, InvalidPrice

# Создаем библиотеку
lib = Library()

# Добавляем книги
try:
    b1 = Book(pages=320, year=2020, author="Александр Пушкин", price=25.5)
    b2 = Book(pages=150, year=2018, author="Федор Достоевский", price=18.0)
    b3 = Book(pages=200, year=2022, author="Александр Пушкин", price=22.0)

    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(b3)

except Exception as e:
    print(f"Ошибка при создании книги: {e}")

# Вывод информации о книге
print(lib.get_book_info(1))
print(lib.get_book_info(99))  # Не существует

# Поиск по автору
pushkin_books = lib.find_by_author("Александр Пушкин")
for book in pushkin_books:
    print(book)

# Поиск по списку авторов
selected_books = lib.find_by_author(["Федор Достоевский", "Александр Пушкин"])
for book in selected_books:
    print(book)

# Сравнение книг по цене
print(b1 > b2)  # True, если цена b1 выше