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
        "search_by_genre",
        "update_all_indexes",   
        "get_library_statistics",
        "sell_pricebook",
        "zakup_pricebook",
    ]
    for i in range(1,steps+1):
        eve=random.choice(events)
        print(eve)
def main():
    run_simulation()
main()
