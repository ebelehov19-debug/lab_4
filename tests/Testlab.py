from src.Labrary import Library
from src.classBook import Book
from src.ClassPriceBook import PriceBook
from src.ClassJournal import Jornal
def test_library_initialization():
    library = Library()
    assert len(library) == 0
    assert len(library.books) == 0
    assert len(library.ind) == 0
    assert repr(library) == "Количество книг в библиотеке 0"

def test_add_book():
    library = Library()
    book = Book("Война и мир", "Лев Толстой", 1869, "Роман", "52")
    result = library.add_book(book)
    assert "Добавлена книга: Война и мир Лев Толстой" == result
    assert len(library) == 1
    assert book in library.books
    assert book.isbn in library.ind.isbn_index
def test_add_books():
    library = Library()
    books = [
        Book("Книга1", "Автор1", 2000, "Жанр1", "1"),
        Book("Книга2", "Автор2", 2001, "Жанр2", "2"),
        Book("Книга3", "Автор3", 2002, "Жанр3", "3"),
    ]
    for book in books:
        library.add_book(book)
    assert len(library) == 3
    for book in books:
        assert book in library.books
def test_remove_book():
    library = Library()
    book = Book("Книга", "Автор", 2000, "Жанр", "ISBN-123")
    library.add_book(book)
    assert len(library) == 1
    result = library.remove_book(book) 
    assert "Удажена книга: Книга Автор" in result
    assert len(library) == 0
    assert book not in library.books
    assert book.isbn not in library.ind.isbn_index

def test_remove_fake_book():
    library = Library()
    book = Book("Книга", "Автор", 2000, "Жанр", "ISBN-123")
    result = library.remove_book(book)
    assert "Книги Книга Автор не было в библиотеке"== result
    assert len(library) == 0
def test_find_by_author():
    library = Library()
    books = [
        Book("Книга1", "Автор1", 2000, "Жанр1", "1"),
        Book("Книга2", "Автор2", 2001, "Жанр2", "2"),
        Book("Книга3", "Автор1", 2002, "Жанр3", "3"),
    ]
    for book in books:
        library.add_book(book)
    found_books = library.find_by_author("Автор1")
    assert len(found_books) == 2
    assert books[0] in found_books
    assert books[1] not in found_books
    assert books[2] in found_books
def test_find_by_year():
    library = Library()
    books = [
        Book("Книга1", "Автор1", 2000, "Жанр1", "1"),
        Book("Книга2", "Автор2", 2000, "Жанр2", "2"),
        Book("Книга3", "Автор1", 2002, "Жанр3", "3"),
    ]
    for book in books:
        library.add_book(book)
    found_books = library.find_by_year(2000)
    assert len(found_books) == 2
    assert books[0] in found_books
    assert books[1] in found_books
    assert books[2] not in found_books
def test_find_by_title():
    library = Library()
    books = [
        Book("Книга1", "Автор1", 2000, "Жанр1", "1"),
        Book("Книга2", "Автор2", 2000, "Жанр2", "2"),
        Book("Книга1", "Автор1", 2002, "Жанр3", "3"),
    ]
    for book in books:
        library.add_book(book)
    found_books = library.find_by_title("Книга1")
    assert len(found_books) == 2
    assert books[0] in found_books
    assert books[2] in found_books
    assert books[1] not in found_books
def test_find_by_year():
    library = Library()
    books = [
        Book("Книга1", "Автор1", 2000, "Жанр1", "1"),
        Book("Книга2", "Автор2", 2000, "Жанр2", "2"),
        Book("Книга3", "Автор1", 2002, "Жанр3", "3"),
    ]
    for book in books:
        library.add_book(book)
    found_books = library.find_by_isbn("1")
    assert found_books == Book("Книга1", "Автор1", 2000, "Жанр1", "1")
def test_repr_method():
    library = Library()
    assert repr(library) == "Количество книг в библиотеке 0"
    book = Book("Книга", "Автор", 2000, "Жанр", "3")
    library.add_book(book)
    assert repr(library) == "Количество книг в библиотеке 1"
   