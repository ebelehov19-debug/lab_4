from src.classBook import Book
from src.listCollect import BookCollection
from src.Classdict import IndexDict
def main():
    book1 = Book("Война и мир", "Лев Толстой", 1869, "Роман", "ISBN-001")
    book2 = Book("Анна Каренина", "Лев Толстой", 1877, "Роман", "ISBN-002")
    print(f"{book1}")
    print(f"{book2}")
    collection = BookCollection()
    collection.add(book1)
    collection.add(book2)
    print(f"Добавлено книг в коллекцию: {len(collection)}")
    print(f"Первая книга: {collection[0]}")
    print(f"Последняя книга: {collection[-1]}")
    index = IndexDict()
    index.update_index(book1)
    index.update_index(book2)
    print(f"Добавлено книг в индекс: {len(index)}")
    print(f"\n   Поиск по ключам:")
    print(f"По ISBN 'ISBN-001': {index['ISBN-001']}")
    print(f"По автору 'Лев Толстой': {len(index['Лев Толстой'])} книг")
    for book in index['Лев Толстой']:
        print(f"- {book}")
    print(f"По году 1949: {len(index[1877])} книг")
    for book in index[1877]:
        print(f"     - {book}")
    print(f"\nИтерация по индексу:")
    print(f" Все ISBN в индексе:")
    for book in index:
        print(f"- {book.isbn}: {book.title}")
    
main()
