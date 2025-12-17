from src.classBook import Book
from src.listCollect import BookCollection
def test_book_collection_initialization():
    collection = BookCollection()
    assert len(collection) == 0
    assert collection.books == []
    assert repr(collection) == "BookCollection имеет 0 книг"
def test_add_single_book():
    collection = BookCollection()
    book = Book("Книга", "Автор", 1869, "Жанр", "52")
    collection.add(book)
    assert len(collection) == 1
    assert book in collection
    assert collection.books[0] == book
    assert repr(collection) == "BookCollection имеет 1 книг"
def test_add_multiple_books():
    collection = BookCollection()
    book1 = Book("Книга1", "Автор1", 2000, "Жанр1", "1")
    book2 = Book("Книга2", "Автор2", 2001, "Жанр2", "2")
    book3 = Book("Книга3", "Автор3", 2002, "Жанр3", "3")
    for book in [book1,book2,book3]:
        collection.add(book)
    assert len(collection) == 3
    assert all(book in collection for book in [book1,book2,book3])
    assert repr(collection) == "BookCollection имеет 3 книг"
def test_getitem_by_index():
    collection = BookCollection()
    book1 = Book("Книга1", "Автор1", 2000, "Жанр1", "1")
    book2 = Book("Книга2", "Автор2", 2001, "Жанр2", "2")
    collection.add(book1)
    collection.add(book2)
    assert collection[0] == book1
    assert collection[1] == book2
    assert collection[-1] == book2
    assert collection[-2] == book1
def test_getitem_slice():
    """Тест 6: Получение среза"""
    collection = BookCollection()
    books = [
        Book("Книга1", "Автор1", 2000, "Жанр1", "1"),
        Book("Книга2", "Автор2", 2001, "Жанр2", "2"),
        Book("Книга3", "Автор3", 2002, "Жанр3", "3"),
        Book("Книга4", "Автор4", 2003, "Жанр4", "4"),
        Book("Книга5", "Автор5", 2004, "Жанр5", "5"),
    ]
    for book in books:
        collection.add(book)
    slice1 = collection[1:4]
    assert len(slice1) == 3
    assert slice1 == books[1:4]
    slice2 = collection[0:5:2]
    assert len(slice2) == 3
    assert slice2 == books[0:5:2]
    slice3 = collection[-3:-1]
    assert len(slice3) == 2
    assert slice3 == books[-3:-1]
    slice4 = collection[2:2]
    assert len(slice4) == 0
    slice5 = collection[:3]
    assert len(slice5) == 3
    assert slice5 == books[:3]
    slice6 = collection[2:]
    assert len(slice6) == 3
    assert slice6 == books[2:]
def test_delite_book():
    collection = BookCollection()
    book1 = Book("Книга1", "Автор1", 2000, "Жанр1", "1")
    book2 = Book("Книга2", "Автор2", 2001, "Жанр2", "2")
    book3 = Book("Книга3", "Автор3", 2002, "Жанр3", "3")
    collection.add(book1)
    collection.add(book2)
    collection.add(book3)
    collection.delite(book2)
    assert len(collection) == 2
    assert book1 in collection
    assert book2 not in collection
    assert book3 in collection
def test_delite_all_books():
    collection = BookCollection()
    book1 = Book("Книга1", "Автор1", 2000, "Жанр1", "1")
    book2 = Book("Книга2", "Автор2", 2001, "Жанр2", "2")
    for book in [book1,book2]:
        collection.add(book)
    for book in [book1,book2]:
        collection.delite(book)
    assert len(collection) == 0
    assert collection.books == []
    assert repr(collection) == "BookCollection имеет 0 книг"
def test_contains():
    collection = BookCollection()
    book1 = Book("Книга1", "Автор1", 2000, "Жанр1", "1")
    book2 = Book("Книга2", "Автор2", 2001, "Жанр2", "2")
    collection.add(book1)
    assert book1 in collection
    assert collection.__contains__(book1) == True
    assert book2 not in collection
    assert collection.__contains__(book2) == False
    assert book1 in collection
    assert Book("new", "Автор", 2000, "Жанр", "ISBN") not in collection
def test_iteration():
    collection = BookCollection()
    book1 = Book("Книга1", "Автор1", 2000, "Жанр1", "1")
    book2 = Book("Книга2", "Автор2", 2001, "Жанр2", "2")
    for book in [book1,book2]:
        collection.add(book)
    iterated_books = []
    for book in collection:
        iterated_books.append(book)
    assert len(iterated_books) == 2
    assert iterated_books == [book1,book2]
    assert list(collection) == [book1,book2]
def test_dubli_books():
    collection = BookCollection()
    book = Book("Книга1", "Автор1", 2000, "Жанр1", "1")
    collection.add(book)
    collection.add(book)
    assert len(collection) == 2
    assert collection[0] == book
    assert collection[1] == book
    collection.delite(book)
    assert len(collection) == 1 
    assert book in collection
def test_repr_method():
    collection = BookCollection()
    assert repr(collection) == "BookCollection имеет 0 книг"
    book = Book("Книга1", "Автор1", 2000, "Жанр1", "1")
    collection.add(book)
    assert repr(collection) == "BookCollection имеет 1 книг"
    collection.add(Book("Книга2", "Автор2", 2001, "Жанр2", "2"))
    assert repr(collection) == "BookCollection имеет 2 книг"