from src.classBook import Book
from src.listCollect import BookCollection
from src.Classdict import IndexDict
from src.ClassJournal import Jornal
from src.ClassPriceBook import PriceBook
from src.Labrary import Library
import random
def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    if seed is not None:
        random.seed(seed)
    library = Library()
    randbook=[
        Book("Война и мир", "Лев Толстой", 1869, "Роман", "1"),
        Book("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", "2"),
        Book("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", "97"),
        Book("1984", "Джордж Оруэлл", 1949, "Антиутопия", "98"),
        Book("Собачье Сердце","Михаил Булгаков", 1967, "Рассказ", "33"),
        Book("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "Фэнтези", "978"),
        Jornal("Наука и жизнь", "Редакция", 2023, "Научный", "123", 80, "month", "Наука"),
        Jornal("Техника молодёжи", "Редакция", 2022, "Технический", "123", 64, "month", "Техника"),
        PriceBook("Python для начинающих", "Иван Иванов", 2022, "Учебник", "987", 1500.0, 10),
        PriceBook("Алгоритмы и структуры данных", "Алексей Петров", 2021, "Учебник", "9874", 2000.0, 5),
        PriceBook("Машинное обучение", "Сергей Сидоров", 2023, "Научный", "9878", 2500.0, 3),
    ]
    for _ in range(5):
        library.add_book(random.choice(randbook))
        print(library)
        events = [
        "add_random_book",
        "remove_random_book", 
        "search_by_author",
        "search_by_year",
        "search_by_isbn",
        "get_library_statistics",
        "get_library_statistics_full",
        "sell_pricebook",
        "check_book",
    ]
    for i in range(1,steps+1):
        eve=random.choice(events)
        print(i,eve)
        if eve==events[0]:
            print(library.add_book(random.choice(randbook)))
        elif eve == events[1]:
            print(library.remove_book(random.choice(randbook)))
        elif eve == events[2]:
            print(f'Информация: {library.find_by_author(random.choice(list(library.ind.author_index.keys())))}')
        elif eve == events[3]:
            print(f'Информация: {library.find_by_year(random.choice(list(library.ind.year_index.keys())))}')
        elif eve == events[4]:
            print(f'Информация: {library.find_by_isbn(random.choice(list(library.ind.isbn_index.keys())))}')
        elif eve == events[5]:
            print(f"Статистика библиотеки:")
            print(f"Всего книг: {len(library)}")
            print(f"Уникальных авторов: {len(library.ind.author_index)}")
            print(f"Уникальных годов: {len(library.ind.year_index)}")
            print(f"Уникальных жанров: {len(library.ind.genre_index)}")
        elif eve == events[6]:
            if library.ind.year_index:
                oldest_year = min(library.ind.year_index.keys())
                newest_year = max(library.ind.year_index.keys())
                print(f"Книги в библиотеке с {oldest_year} года по {newest_year} год")
            if library.ind.author_index:
                popular_author = max(library.ind.author_index.items(),key=lambda x: len(x[1]))
                print(f"Самый популярный автор в библиотеке {popular_author[0]} {len(popular_author[1])} книг")
            if library.ind.genre_index:
                    popular_genre = max(library.ind.genre_index.items(), key=lambda x: len(x[1]))
                    print(f"Самый популярный жанр в библиотеке {popular_genre[0]} {len(popular_genre[1])} книг")
        elif eve == events[7]:
            pb = [b for b in library.books if isinstance(b, PriceBook) and b.is_for_sale]
            if len(pb)>0:
                book_to_sell = random.choice(pb)
                max_sell = min(book_to_sell.quantity, 5)
                quantity = random.randint(1, max_sell) if max_sell > 0 else 1  
                result = book_to_sell.sell(quantity)
                print(f"{result}")
            else:
                print("В библиотеке нет книг для продажи")
        elif eve == events[8]:
            random_book = random.choice(library.books)
            print(f"Проверка доступности книги:")
            print(f"Название: {random_book.title}")
            print(f"Автор: {random_book.author}")                
            if isinstance(random_book, PriceBook):
                print("Тип: Книга для продажи")
                print(f"Доступна для продажи: {'Да' if random_book.is_for_sale else 'Нет'}")
                print(f"В наличии: {random_book.quantity} шт.")
                print(f"Цена: {random_book.price:.2f} руб.")
                print(f"Продано всего: {random_book.total_sold} шт.")
                print(f"Выручка: {random_book.total_revenue:.2f} руб.")
            elif isinstance(random_book, Jornal):
                print(f"Тип: Журнал")
                print(f"Страниц: {random_book.pages}")
                print(f"Периодичность: {random_book.period}")
                print(f"Издательство: {random_book.publesher}")
            else:
                print(f"Тип: Обычная книга")
def main():
    print("Приветствую!!! Это симуляция работы  библиотеки! Формат входных данных: первое число - это количество шагов в симуляции, ф второе для повторного воспроизведение симуляции. Для завершения напишите exit")
    while (a := input()) != 'exit':
        try:
            s = a.split()
            if len(s) == 2:
                run_simulation(int(s[0]), int(s[1]))
                print("Работа симуляции завершилась. Можете ввести еще данные для работы симуляции или выйти, написав 'exit'")
            elif len(s) == 1:
                run_simulation(int(s[0]))
                print("Работа симуляции завершилась. Можете ввести еще данные для работы симуляции или выйти, написав 'exit'")
            elif len(s) == 0:
                print("Введите значение")
            else:
                print("Некорректное количество значений")
        except ValueError as e:
            print(f"Ошибка преобразования данных: {e} введите целые числа.")
    print("Использование симуляции завершено! Спасибо за использование! Хорошего дня!")

main()
