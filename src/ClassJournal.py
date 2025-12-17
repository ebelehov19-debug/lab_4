from src.classBook import Book
class Jornal(Book):
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, pages: int, period: str = "month",publesher: str = ""):
        super().__init__(title, author, year, genre, isbn)
        self.pages = pages
        self.period = period
        self.publesher = publesher
    def __repr__(self) -> str:
        return f"Журнал '{self.title}' дата выхода первого издания {self.year},издательство {self.publesher} количество страниц {self.pages}, период выпуска {self.period})"
    def full_info(self) -> str:
        """Получить полную информацию о журнале"""
        return (f"{self.title} - {self.author}  {self.year} количество страниц: {self.pages}, период выхода: {self.period}, издательство {self.publesher}")
    def size(self)->None:
        "Длинна журнала в страницах"
        return f"Количество страниц в журнале {self.pages}"
    def change_publesher(self, new_publesher: str) -> None:
        old_publesher = self.publesher
        self.publesher = new_publesher
        return f"Издательство изменено с '{old_publesher}' на '{new_publesher}'"
    def cnt_jornal_yers(self)-> None:
        period={'month':12,'year':1,'week':52,'day':365}
        return f"Журнал {self.title} за год вышел {period[self.period]} раз"
    