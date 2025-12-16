from src.classBook import Book
from src.listCollect import BookCollection
from src.Classdict import IndexDict
from src.Labrary import Library
def main():
    book1 = Book("Война и мир", "Лев Толстой", 1869, "Роман", "978-5-389-12345-6")
    book2 = Book("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", "978-5-389-12346-3")
    lib=Library()
    lib.add_book(book1)
    lib.add_book(book2)
    print("Поиск по автору 'Лев Толстой':")
    tolstoy_books = lib.find_by_author("Лев Толстой")
    for book in tolstoy_books:
        print(f" - {book.title} ({book.year})")
main()
