import psycopg
import config
from providers.data_provider import DataProvider
from db_logic.raw_sql_queries import (CREATE_TABLE_QUERIES, INSERT_AUTHOR, INSERT_BOOK, INSERT_GENRE, 
                                      INSERT_BOOK_GENRE, SELECT_BOOK_BY_GENRE, SELECT_BOOK_BY_AUTHOR_AND_YEAR)


class RawSqlProvider(DataProvider):
    connection = None

    @staticmethod
    def connect():
        if not RawSqlProvider.connection or RawSqlProvider.connection.closed:
            print('Create new connection')
            RawSqlProvider.connection = psycopg.connect(
                f"dbname={config.DB_NAME} user={config.DB_USER} password={config.DB_PASSWORD} host={config.DB_HOST}")
            return RawSqlProvider.connection
        
        print('Use existing connections')
        return RawSqlProvider.connection

    @staticmethod
    def create_tables():
        with RawSqlProvider.connect() as conn:
            with conn.cursor() as cur:
                for q in CREATE_TABLE_QUERIES:
                    cur.execute(q)

    @staticmethod
    def add_author(name):
        with RawSqlProvider.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(INSERT_AUTHOR, (name,))
                return cur.fetchone()[0]

    @staticmethod
    def add_book(*args):
        title, publication_year, author_id = args
        with RawSqlProvider.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(INSERT_BOOK, (title, publication_year, author_id))
                return cur.fetchone()[0]
            
    @staticmethod
    def add_genre(genre_name):
        with RawSqlProvider.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(INSERT_GENRE, (genre_name, ))
                return cur.fetchone()[0]

    @staticmethod
    def add_book_genre(book_id, genre_id):
        with RawSqlProvider.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(INSERT_BOOK_GENRE, (book_id, genre_id))
                return cur.fetchone()

    @staticmethod
    def get_books_by_genre(genre_name):
        with RawSqlProvider.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(SELECT_BOOK_BY_GENRE, (f'%{genre_name}%',))
                return cur.fetchall()

    @staticmethod
    def get_books_by_author_and_year(author_name, year):
        with RawSqlProvider.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(SELECT_BOOK_BY_AUTHOR_AND_YEAR, (f'%{author_name}%', year))
                return cur.fetchall()

