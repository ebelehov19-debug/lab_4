class BookCollection:
    def __init__(self) -> None:
        """Создает пустую коллекцию книг"""
        self.books = []
    def __len__(self) -> int:
        """Возвращает количество книг в коллекции"""
        return len(self.books) 
    def __iter__(self) -> iter:
        """Итерируется по книгам в коллекции"""
        return iter(self.books)
    def __getitem__(self, index) -> list:
        """Получает книгу или срез книг по индексу"""
        if isinstance(index, slice):
            return self.books[index.start:index.stop:index.step]
        if index < 0:
            index = len(self.books) + index
        if 0 <= index < len(self.books):
            return self.books[index]    
        raise IndexError(f"Индекс вне допустимого диапазона диапазона")
    def add(self, val) -> None:
        """Добавляет книгу в коллекцию"""
        self.books.append(val)
    def delite(self, book) -> None:
        """Удаляет книгу из коллекции"""
        if book in self.books:
            self.books.remove(book)
    def __contains__(self, book) -> bool:
        """Проверяет есть ли книга в коллекции"""
        return book in self.books
    def __repr__(self) -> str:
        """Строковое представление коллекции"""
        return f"BookCollection имеет {len(self.books)} книг"