from src.Classdict import IndexDict
from src.classBook import Book
def test_index_dict_initialization():
    index = IndexDict()
    assert len(index) == 0
    assert index.isbn_index == {}
    assert index.author_index == {}
    assert index.year_index == {}
    assert index.title_index == {}
    assert index.genre_index == {}
def test_update_index_book():
    index = IndexDict()
    book = Book("Война и мир", "Лев Толстой", 1869, "Роман", "52-67") 
    index.update_index(book)
    assert len(index) == 1
    assert book.isbn in index.isbn_index
    assert index.isbn_index[book.isbn] == book
    assert book.author in index.author_index
    assert book in index.author_index[book.author]
    assert len(index.author_index[book.author]) == 1
    assert book.year in index.year_index
    assert book in index.year_index[book.year]
    assert len(index.year_index[book.year]) == 1
    assert book.title in index.title_index
    assert book in index.title_index[book.title]
    assert len(index.title_index[book.title]) == 1
    assert book.genre in index.genre_index
    assert book in index.genre_index[book.genre]
    assert len(index.genre_index[book.genre]) == 1
def test_update_index_books():
    index = IndexDict()
    book1 = Book("Книга1", "Автор1", 2000, "Жанр1", "1")
    book2 = Book("Книга2", "Автор2", 2000, "Жанр1", "2")
    book3 = Book("Книга3", "Автор1", 2001, "Жанр2", "3")
    index.update_index(book1)
    index.update_index(book2)
    index.update_index(book3)
    assert len(index) == 3
    assert len(index.author_index["Автор1"]) == 2
    assert book1 in index.author_index["Автор1"]
    assert book3 in index.author_index["Автор1"]
    assert len(index.author_index["Автор2"]) == 1
    assert len(index.year_index[2000]) == 2
    assert book1 in index.year_index[2000]
    assert book2 in index.year_index[2000]
    assert len(index.year_index[2001]) == 1
    assert len(index.genre_index["Жанр1"]) == 2
    assert book1 in index.genre_index["Жанр1"]
    assert book2 in index.genre_index["Жанр1"]
    assert len(index.genre_index["Жанр2"]) == 1
def test_update_index_books_rep():
    index = IndexDict()
    book = Book("Книга", "Автор", 2000, "Жанр", "ISBN-123")
    index.update_index(book)
    index.update_index(book)
    assert len(index) == 1
    assert len(index.author_index["Автор"]) == 1
    assert len(index.year_index[2000]) == 1
    assert len(index.title_index["Книга"]) == 1
    assert len(index.genre_index["Жанр"]) == 1
def test_remove_book():
    index = IndexDict()
    book1 = Book("Книга1", "Автор1", 2000, "Жанр1", "1")
    book2 = Book("Книга2", "Автор1", 2000, "Жанр1", "2")
    index.update_index(book1)
    index.update_index(book2)
    index.remove_book(book1)
    assert len(index) == 1
    assert book1.isbn not in index.isbn_index
    assert book2.isbn in index.isbn_index
    assert len(index.author_index["Автор1"]) == 1
    assert book1 not in index.author_index["Автор1"]
    assert book2 in index.author_index["Автор1"]
    index.remove_book(book2)
    assert len(index) == 0
    assert len(index.author_index) == 0
    assert len(index.year_index) == 0
    assert len(index.title_index) == 0
    assert len(index.genre_index) == 0
def test_removes__book():
    index = IndexDict()
    book = Book("Книга", "Автор", 2000, "Жанр", "1")
    index.remove_book(book) 
    index.update_index(book)
    index.remove_book(book)
    assert len(index) == 0
def test_getitem_by_isbn():
    index = IndexDict()
    book = Book("Книга", "Автор", 2000, "Жанр", "1")
    index.update_index(book)
    result = index[book.isbn]
    assert result == book
    try:
        index["fake"]
    except KeyError as e:
        assert "не найден" in str(e)
def test_getitem_by_author():
    index = IndexDict()
    book1 = Book("Книга1", "Автор", 2000, "Жанр", "1")
    book2 = Book("Книга2", "Автор", 2001, "Жанр", "2")
    index.update_index(book1)
    index.update_index(book2)
    author_books = index["Автор"]
    assert len(author_books) == 2
    assert book1 in author_books
    assert book2 in author_books
def test_getitem_by_year():
    index = IndexDict()
    book1 = Book("Книга1", "Автор", 2000, "Жанр", "1")
    book2 = Book("Книга2", "Автор", 2000, "Жанр", "2")
    index.update_index(book1)
    index.update_index(book2)
    year_books = index[2000]
    assert len(year_books) == 2
    assert book1 in year_books
    assert book2 in year_books
    try:
        index[52]
    except KeyError as e:
        assert "не найден" in str(e)
def test_getitem_by_title():
    index = IndexDict()
    book = Book("new", "Автор", 2000, "Жанр", "3") 
    index.update_index(book)
    title_books = index["new"]
    assert isinstance(title_books, list)
    assert len(title_books) == 1
    assert book in title_books
def test_getitem_by_genre():
    index = IndexDict()
    book1 = Book("Книга1", "Автор1", 2000, "Роман", "1")
    book2 = Book("Книга2", "Автор2", 2001, "Роман", "2")
    index.update_index(book1)
    index.update_index(book2)
    genre_books = index["Роман"]
    assert len(genre_books) == 2
    assert book1 in genre_books
    assert book2 in genre_books
def test_find_by_author():
    index = IndexDict()
    book1 = Book("Книга 1", "Лев Толстой", 1869, "Роман", "1")
    book2 = Book("Книга 2", "Фёдор Достоевский", 1866, "Роман", "2")
    book3 = Book("Книга 3", "Лев Толстой", 1873, "Роман", "3")
    for book in [book1, book2, book3]:
        index.update_index(book)
    tolstoy_books = index.find_by_author("Лев Толстой")
    assert len(tolstoy_books) == 2
    assert book1 in tolstoy_books
    assert book3 in tolstoy_books
    dostoevsky_books = index.find_by_author("Фёдор Достоевский")
    assert len(dostoevsky_books) == 1
    assert book2 in dostoevsky_books
    nonexistent = index.find_by_author("Неизвестныйавтор")
    assert nonexistent == []
    assert len(nonexistent) == 0
def test_find_by_year():
    index = IndexDict()
    book1 = Book("Книга1", "Автор", 2000, "Жанр", "1")
    book2 = Book("Книга2", "Автор", 2000, "Жанр", "2")
    book3 = Book("Книга3", "Автор", 2001, "Жанр", "3") 
    for book in [book1, book2, book3]:
        index.update_index(book)
    year_2000_books = index.find_by_year(2000)
    assert len(year_2000_books) == 2
    assert book1 in year_2000_books
    assert book2 in year_2000_books
    year_2001_books = index.find_by_year(2001)
    assert len(year_2001_books) == 1
    assert book3 in year_2001_books
    year_52_books = index.find_by_year(52)
    assert year_52_books == []
    assert len(year_52_books) == 0
def test_find_by_title():
    index = IndexDict()
    book1 = Book("Война и мир", "Лев Толстой", 1869, "Роман", "1")
    book2 = Book("Война и мир 2", "Лев Толстой", 1869, "Роман", "2")
    index.update_index(book1)
    index.update_index(book2)
    war = index.find_by_title("Война и мир")
    assert len(war) == 1
    assert book1 in war
    war2 = index.find_by_title("Война и мир 2")
    assert len(war2) == 1
    assert book2 in war2
    nonexistent = index.find_by_title("Капитанская дочка")
    assert nonexistent == []
    assert len(nonexistent) == 0
def test_find_by_isbn():
    index = IndexDict()
    book = Book("Книга", "Автор", 2000, "Жанр", "123")
    index.update_index(book)
    found_book = index.find_by_isbn("123")
    assert found_book == book
    not_found = index.find_by_isbn("52-е")
    assert not_found == []
    assert len(not_found) == 0
def test_find_by_genre():
    index = IndexDict()
    book1 = Book("Книга1", "Автор1", 2000, "Фантастика", "1")
    book2 = Book("Книга2", "Автор2", 2001, "Фантастика", "2")
    book3 = Book("Книга3", "Автор3", 2002, "Детектив", "3")
    for book in [book1, book2, book3]:
        index.update_index(book)
    fantasy_books = index.find_by_genre("Фантастика")
    assert len(fantasy_books) == 2
    assert book1 in fantasy_books
    assert book2 in fantasy_books
    detective_books = index.find_by_genre("Детектив")
    assert len(detective_books) == 1
    assert book3 in detective_books
    nonexistent = index.find_by_genre("привет")
    assert nonexistent == []
    assert len(nonexistent) == 0
def test_iter_method():
    index = IndexDict()
    book1=Book("Книга 1", "Автор 1", 2000, "Жанр 1", "1")
    book2=Book("Книга 2", "Автор 2", 2001, "Жанр 2", "2")
    book3=Book("Книга 3", "Автор 3", 2002, "Жанр 3", "3")
    for book in [book1, book2, book3]:
        index.update_index(book)
    iter = list(index)
    assert len(iter) == 3
    for book in [book1, book2, book3]:
        assert book in iter
    empty_index = IndexDict()
    assert len(list(empty_index)) == 0
def print_all():
    index = IndexDict()
    book1 = Book("Книга1", "Автор1", 2000, "Фантастика", "1")
    book2 = Book("Книга2", "Автор2", 2001, "Фантастика", "2")
    book3 = Book("Книга3", "Автор3", 2002, "Детектив", "3")
    for book in [book1, book2, book3]:
        index.update_index(book)
    all_books = index.print_all_books()
    assert isinstance(all_books, list)
    assert len(all_books) == 3
def test_clear_library():
    index = IndexDict()
    book1 = Book("Книга1", "Автор1", 2000, "Жанр1", "1")
    book2 = Book("Книга2", "Автор2", 2001, "Жанр2", "2")
    index.update_index(book1)
    index.update_index(book2)
    assert len(index) == 2
    assert len(index.author_index) == 2
    assert len(index.year_index) == 2
    assert len(index.title_index) == 2
    assert len(index.genre_index) == 2
    index.clear_library()
    assert len(index) == 0
    assert len(index.author_index) == 0
    assert len(index.year_index) == 0
    assert len(index.title_index) == 0
    assert len(index.genre_index) == 0   
