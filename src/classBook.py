class Book:
    """Класс, представляющий книгу в библиотечной системе."""
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        """Создает новый объект книги с заданными атрибутами."""
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
    def __repr__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"'{self.title}', '{self.author}', {self.year}, '{self.genre}', '{self.isbn}'"
    def __eq__(self, other) -> bool:
        """Сравнивает две книги по ISBN номеру."""
        if not isinstance(other, Book):
            return False
        return self.isbn == other.isbn