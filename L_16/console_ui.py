import sys

from providers.data_provider import DataProvider

ACTION_ITEMS = """
Choose action item from the list:
    1. add author
    2. add book
    3. add genre
    4. add book genre
    5. get book by genre
    6. get book by author and year
    7. exit
"""


class ConsoleDbApp:
    def __init__(self, raw_data_provider, orm_data_provider):
        self.data_provider: DataProvider | None = None
        self.raw_data_provider = raw_data_provider
        self.orm_data_provider = orm_data_provider

    def start_app(self):
        choose = int(input('Choose data provider for initialization: 1 - raw 2 - orm '))
        self.data_provider = self.raw_data_provider if choose == 1 else self.orm_data_provider

        print('Starting ConsoleApp ...')
        self.data_provider.create_tables() 

        while True:
            action_item = int(input(ACTION_ITEMS))

            match action_item:
                case 1: 
                    author_name = input('Enter author name: ')
                    author_id = self.data_provider.add_author(author_name)
                    print(f"Author added, id: {author_id}")
                case 2:
                    title, publication_year, author_id = input('Enter book title, publication_year, author_id').split(',')
                    author_id = self.data_provider.add_book(title, publication_year, author_id)
                    print(f"Book added, id: {author_id}")
                case 3:
                    genre_name = input('Enter genre name: ')
                    genre_id = self.data_provider.add_genre(genre_name)
                    print(f"Genre added: {genre_id}")
                case 4:
                    book_id, genre_id = input('Enter book_id and genre_id').split(', ')
                    book_id, genre_id = self.data_provider.add_book_genre(book_id, genre_id)
                    print(f"Book with id: {book_id} linked to genre with id: {genre_id}")
                case 5:
                    genre = input('Enter book genre: ')
                    book_titles = self.data_provider.get_books_by_genre(genre)
                    if book_titles:
                        for title in book_titles:
                            print(f'Book title: {title}')
                    else:
                        print('Books not found')
                case 6:
                    author, publication_year = input('Enter book author and publication_year: ').split(', ')
                    books = self.data_provider.get_books_by_author_and_year(author, publication_year)
                    if books:
                        for book in books:
                            print(f'{book[0], book[1], book[2]}')
                    else:
                        print('Books not found')
                case 7:
                    print('Finishing work ...')
                    sys.exit()