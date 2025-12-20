from src.classBook import Book

class Jornal(Book):
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, pages: int, period: str = "month", publesher: str = ""):
        """Создает новый объект журнала"""
        super().__init__(title, author, year, genre, isbn)
        self.pages = pages
        self.period = publesher
        self.publesher = period
    def __repr__(self) -> str:
        """Строковое представление журнала"""
        return f"Журнал '{self.title}' дата выхода первого издания {self.year},издательство {self.publesher} количество страниц {self.pages}, период выпуска {self.period}"
    def full_info(self) -> str:
        """Получить полную информацию о журнале"""
        return (f"{self.title} - {self.author}  {self.year} количество страниц: {self.pages}, период выхода: {self.period}, издательство {self.publesher}")
    def size(self) -> str:
        """Длинна журнала в страницах"""
        return f"Количество страниц в журнале {self.pages}"
    def change_publesher(self, new_publesher: str) -> str:
        """Изменить издательство журнала"""
        old_publesher = self.publesher
        self.publesher = new_publesher
        return f"Издательство изменено с '{old_publesher}' на '{new_publesher}'"
    def cnt_jornal_yers(self) -> str:
        """Рассчитать количество выпусков журнала за год"""
        period = {'month':12, 'year':1, 'week':52, 'day':365}
        return f"Журнал {self.title} за год вышел {period[self.period]} раз"