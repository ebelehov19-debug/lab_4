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
    print(f"\n2. Состояние библиотеки: {lib}")
    print(f"   Количество книг: {len(lib.books)}")
    print("\n3. Проверка индексов:")
    print(f"Книг в индексе: {len(lib.ind)}")
    print(f"Книга по ISBN 978-5-389-12345-6: {'978-5-389-12345-6' in lib.ind}")
    print("\n5. Удаление книги:")
    lib.remove_book(book1) 
    lib.remove_book(book1)
main()
