from src.ClassJournal import Jornal
from src.classBook import Book
def test_jornal_init():
    jornal = Jornal(
        title="Наука и жизнь",
        author="Редакция",
        year=2023,
        genre="Научный",
        isbn="52",
        pages=80
    )
    assert jornal.title == "Наука и жизнь"
    assert jornal.author == "Редакция"
    assert jornal.year == 2023
    assert jornal.genre == "Научный"
    assert jornal.isbn == "52"
    assert jornal.pages == 80
    assert jornal.period == "month"  
    assert jornal.publesher == ""  
def test_jornal_in_book():
    jornal = Jornal("Журнал", "Автор", 2023, "Жанр", "1", 100)
    assert isinstance(jornal, Book)
    assert isinstance(jornal, Jornal)
    assert hasattr(jornal, 'title')
    assert hasattr(jornal, 'author')
    assert hasattr(jornal, 'year')
    assert hasattr(jornal, 'genre')
    assert hasattr(jornal, 'isbn')
    book = Book("Журнал", "Автор", 2023, "Жанр", "1")
    assert jornal == book  
def test_jornal_repr():
    jornal = Jornal(
        title="Наука и жизнь",
        author="Редакция",
        year=2023,
        genre="Научный",
        isbn="1",
        pages=82,
        period="month",
        publesher="NG"
    )
    repr_str = repr(jornal)
    assert "Журнал 'Наука и жизнь'" in repr_str
    assert "2023" in repr_str
    assert "NG" in repr_str
    assert "82" in repr_str
    assert "month" in repr_str
def test_full_info():
    jornal = Jornal(
        title="Наука и жизнь",
        author="Редакция",
        year=2023,
        genre="Научный",
        isbn="1",
        pages=82,
        period="month",
        publesher="NG"
    )
    info = jornal.full_info()
    assert "Наука и жизнь" in info
    assert "Редакция" in info
    assert "2023" in info
    assert "82" in info
    assert "month" in info
    assert "NG" in info
def test_size_method():
    jornal = Jornal("Журнал", "Автор", 2023, "Жанр", "1", 120)
    size_str= jornal.size()
    assert size_str == "Количество страниц в журнале 120"
def test_change_publesher():
    jornal = Jornal(
        title="Наука и жизнь",
        author="Редакция",
        year=2023,
        genre="Научный",
        isbn="1",
        pages=82,
        period="month",
        publesher="NG"
    )
    s=jornal.change_publesher('new')
    assert s == "Издательство изменено с 'NG' на 'new'"
def test_cnt_jornal():
    jornal = Jornal("Журнал", "Автор", 2023, "Жанр", "52", 100, "month")
    s=jornal.cnt_jornal_yers()
    assert s== "Журнал Журнал за год вышел 12 раз"
