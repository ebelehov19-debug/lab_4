from src.Classdict import IndexDict
from src.listCollect import BookCollection
class Library:
    def __init__(self):
        self.books = BookCollection()
        self.ind = IndexDict()
    def __repr__(self) -> str:
        return f"Количество книг в библиотеке {len(self.books)}"
    def __len__(self):
        return len(self.books)
    def add_book(self,book):
        if book not in self.books:
            self.books.add(book)
            self.ind.update_index(book)
            print(f"Добавлена книга: {book.title} {book.author}")
        else:
            print(f"Книга '{book.title}' уже есть в библиотеке")
    def remove_book(self,book):
        if book in self.books:
            self.books.delite(book)
            self.ind.remove_book(book)
            print(f"Удажена книга: {book.title} {book.author}")
        else:
            print(f"Книги {book.title} {book.author} не было в библиотеке")
