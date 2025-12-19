from src.Classdict import IndexDict
from src.listCollect import BookCollection

class Library:
    def __init__(self):
        """Создает библиотеку с коллекцией книг и индексами"""
        self.books = BookCollection()
        self.ind = IndexDict()
    def __repr__(self) -> str:
        """Строковое представление библиотеки"""
        return f"Количество книг в библиотеке {len(self.books)}"
    def __len__(self):
        """Возвращает количество книг в библиотеке"""
        return len(self.books)
    def add_book(self, book):
        """Добавляет книгу в библиотеку"""
        if book not in self.books:
            self.books.add(book)
            self.ind.update_index(book)
            return f"Добавлена книга: {book.title} {book.author}"
        else:
            return f"Книга '{book.title}' уже есть в библиотеке"
    def remove_book(self, book):
        """Удаляет книгу из библиотеки"""
        if book in self.books:
            self.books.delite(book)
            self.ind.remove_book(book)
            return f"Удажена книга: {book.title} {book.author}"
        else:
            return f"Книги {book.title} {book.author} не было в библиотеке"
    def find_by_author(self, author: str):
        """Находит книги по автору"""
        books = self.ind.find_by_author(author)
        print(f"У авторф '{author}' найдено {len(books)} книг")
        return books
    def find_by_year(self, year: int):
        """Находит книги по году издания"""
        books = self.ind.find_by_year(year)
        print(f"По году {year} найдено {len(books)} книг")
        return books  
    def find_by_title(self, title: str):
        """Находит книги по названию"""
        books = self.ind.find_by_title(title)
        print(f"По названию '{title}' найдено {len(books)} книг")
        return books
    def find_by_isbn(self, isbn: str):
        """Находит книгу по ISBN"""
        books = self.ind.find_by_isbn(isbn)
        print(f"По ISBN '{isbn}' найдено")
        return books