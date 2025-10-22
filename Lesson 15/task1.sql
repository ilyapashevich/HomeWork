-- Таблица authors
CREATE TABLE authors (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);

-- Таблица books
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author_id INTEGER,
    publication_year INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

-- Таблица sales
CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    book_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (book_id) REFERENCES books(id)
);

-- Добавление авторов
INSERT INTO authors (id, first_name, last_name) VALUES
(1, 'George', 'Orwell'),
(2, 'Jane', 'Austen'),
(3, 'Mark', 'Twain'),
(4, 'Unknown', 'Author');

-- Добавление книг
INSERT INTO books (id, title, author_id, publication_year) VALUES
(1, '1984', 1, 1949),
(2, 'Animal Farm', 1, 1945),
(3, 'Pride and Prejudice', 2, 1813),
(4, 'Adventures of Huckleberry Finn', 3, 1884),
(5, 'Mystery Book', NULL, 2000); -- книга без автора

-- Добавление продаж
INSERT INTO sales (id, book_id, quantity) VALUES
(1, 1, 120),
(2, 2, 85),
(3, 3, 60),
(4, 4, 95),
(5, 5, 30);

-- INNER JOIN: книги и их авторы
SELECT books.title, authors.first_name, authors.last_name
FROM books
INNER JOIN authors ON books.author_id = authors.id;

-- LEFT JOIN: все авторы и их книги
SELECT authors.first_name, authors.last_name, books.title
FROM authors
LEFT JOIN books ON authors.id = books.author_id;

-- RIGHT JOIN: все книги и их авторы
SELECT books.title, authors.first_name, authors.last_name
FROM books
RIGHT JOIN authors ON books.author_id = authors.id;

-- INNER JOIN: книги, авторы и продажи
SELECT books.title, authors.first_name, authors.last_name, sales.quantity
FROM books
INNER JOIN authors ON books.author_id = authors.id
INNER JOIN sales ON books.id = sales.book_id;

-- LEFT JOIN: авторы, книги и продажи (включая NULL)
SELECT authors.first_name, authors.last_name, books.title, sales.quantity
FROM authors
LEFT JOIN books ON authors.id = books.author_id
LEFT JOIN sales ON books.id = sales.book_id;

-- INNER JOIN + агрегат: общее количество продаж по авторам
SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sales
FROM authors
INNER JOIN books ON authors.id = books.author_id
INNER JOIN sales ON books.id = sales.book_id
GROUP BY authors.id;

-- LEFT JOIN + агрегат: включая авторов без продаж
SELECT authors.first_name, authors.last_name, COALESCE(SUM(sales.quantity), 0) AS total_sales
FROM authors
LEFT JOIN books ON authors.id = books.author_id
LEFT JOIN sales ON books.id = sales.book_id
GROUP BY authors.id;

-- Автор с наибольшим количеством проданных книг
SELECT first_name, last_name
FROM (
    SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sales
    FROM authors
    JOIN books ON authors.id = books.author_id
    JOIN sales ON books.id = sales.book_id
    GROUP BY authors.id
) AS author_sales
ORDER BY total_sales DESC
LIMIT 1;

-- Книги, проданные выше среднего
SELECT books.title, sales.quantity
FROM books
JOIN sales ON books.id = sales.book_id
WHERE sales.quantity > (
    SELECT AVG(quantity) FROM sales
);
