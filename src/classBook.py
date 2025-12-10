class Book:
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
    def __repr__(self) -> str:
        return f"Book('{self.title}', '{self.author}', {self.year}, '{self.genre}', '{self.isbn}')"
    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return False
        return self.isbn == other.isbn


