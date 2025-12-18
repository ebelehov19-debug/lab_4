class IndexDict:
    """Класс для индексированного хранения книг по различным критериям."""
    
    def __init__(self) -> None:
        """Создает пустые индексы для хранения книг."""
        self.isbn_index = {}
        self.author_index = {}
        self.year_index = {}
        self.title_index = {}
        self.genre_index = {}
    
    def __len__(self) -> int:
        """Возвращает общее количество книг."""
        return len(self.isbn_index)
    
    def __iter__(self) -> iter:
        """Итерируется по всем книгам в библиотеке."""
        return iter(self.isbn_index.values())
    
    def __getitem__(self, key: str) -> 'Book' or list:
        """Находит книги по ключу (ISBN, автор, название, жанр или год)."""
        if isinstance(key, str):
            if key in self.isbn_index:
                return self.isbn_index[key]
            elif key in self.author_index:
                return self.author_index[key]  
            elif key in self.title_index:
                return self.title_index[key]
            elif key in self.genre_index:
                return self.genre_index[key]
        elif isinstance(key, int):
            if key in self.year_index:
                return self.year_index[key] 
        raise KeyError(f"Ключ '{key}' не найден в словаре")
    
    def __repr__(self) -> str:
        """Строковое представление состояния библиотеки."""
        return f'В библиотеке {len(self.isbn_index)} книг, авторов {len(self.author_index)}, жанров {len(self.genre_index)}'
    
    def update_index(self, book) -> None:
        """Добавляет книгу во все индексы."""
        self.isbn_index[book.isbn] = book

        if book.author not in self.author_index:
            self.author_index[book.author] = []
        if book not in self.author_index[book.author]:
            self.author_index[book.author].append(book)

        if book.year not in self.year_index:
            self.year_index[book.year] = []
        if book not in self.year_index[book.year]:
            self.year_index[book.year].append(book)

        if book.title not in self.title_index:
            self.title_index[book.title] = []
        if book not in self.title_index[book.title]:
            self.title_index[book.title].append(book)

        if book.genre not in self.genre_index:
            self.genre_index[book.genre] = []
        if book not in self.genre_index[book.genre]:
            self.genre_index[book.genre].append(book)
    
    def remove_book(self, book) -> None:
        """Удаляет книгу из всех индексов."""
        if book.isbn in self.isbn_index:
            del self.isbn_index[book.isbn]
        
        if book.author in self.author_index:
            if book in self.author_index[book.author]:
                self.author_index[book.author].remove(book)
                if not self.author_index[book.author]:
                    del self.author_index[book.author]

        if book.year in self.year_index:
            if book in self.year_index[book.year]:
                self.year_index[book.year].remove(book)
                if not self.year_index[book.year]:
                    del self.year_index[book.year]

        if book.title in self.title_index:
            if book in self.title_index[book.title]:
                self.title_index[book.title].remove(book)
                if not self.title_index[book.title]:
                    del self.title_index[book.title]
        
        if book.genre in self.genre_index:
            if book in self.genre_index[book.genre]:
                self.genre_index[book.genre].remove(book)
                if not self.genre_index[book.genre]:
                    del self.genre_index[book.genre]
    
    def find_by_author(self, author: str) -> list:
        """Находит книги по автору."""
        return self.author_index.get(author, [])   
    
    def find_by_year(self, year: int) -> list:
        """Находит книги по году издания."""
        return self.year_index.get(year, [])    
    
    def find_by_title(self, title: str) -> list:
        """Находит книги по названию."""
        return self.title_index.get(title, [])
    
    def find_by_isbn(self, isbn: str) -> list:
        """Находит книгу по ISBN."""
        return self.isbn_index.get(isbn, [])
    
    def find_by_genre(self, genre: str) -> list:
        """Находит книги по жанру."""
        return self.genre_index.get(genre, [])
    
    def print_all_books(self) -> list:
        """Возвращает список всех книг."""
        return list(self.isbn_index.values())
    
    def clear_library(self) -> None:
        """Очищает все индексы."""
        self.isbn_index.clear()
        self.title_index.clear()
        self.genre_index.clear()
        self.author_index.clear()
        self.year_index.clear()