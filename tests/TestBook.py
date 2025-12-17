from src.classBook import Book
def test_book_initialization():
    book = Book(
        title="Война и мир",
        author="Лев Толстой",
        year=1869,
        genre="Роман",
        isbn="52"
    )
    assert book.title == "Война и мир"
    assert book.author == "Лев Толстой"
    assert book.year == 1869
    assert book.genre == "Роман"
    assert book.isbn == "52"
def test_book_with_empty():
    book = Book("", "", 0, "", "")
    assert book.title == ""
    assert book.author == ""
    assert book.year == 0
    assert book.genre == ""
    assert book.isbn == ""
def test_repr_method():
    book = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", "52")
    repr_str = repr(book)
    assert "Мастер и Маргарита" in repr_str
    assert "Михаил Булгаков" in repr_str
    assert "1967" in repr_str
    assert "Роман" in repr_str
    assert "52" in repr_str
    exp= "Book('Мастер и Маргарита', 'Михаил Булгаков', 1967, 'Роман', '52')"
    assert repr_str == exp
def test_eq():
    book1 = Book("Книга", "Автор", 2000, "Жанр", "1")
    book2 = Book("Книга", "Автор", 2000, "Жанр", "1")
    assert book1 == book2
    assert book2 == book1
def test_eq_different_isbn():
    book1 = Book("Книга", "Автор", 2000, "Жанр", "1")
    book2 = Book("Книга", "Автор", 2000, "Жанр", "2")
    assert book1 != book2
    assert book2 != book1