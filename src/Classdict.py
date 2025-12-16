class IndexDict:
    def __init__(self):
        self.isbn_index = {}
        self.author_index = {}
        self.year_index = {}
        self.title_index = {}
    def __len__(self):
        return len(self.isbn_index)
    def __iter__(self):
        return iter(self.isbn_index.values())
    def __getitem__(self, key: str):
        if isinstance(key, str):
            if key in self.isbn_index:
                return self.isbn_index[key]
            elif key in self.author_index:
                return self.author_index[key]  
            elif key in self.title_index:
                return self.title_index[key]
        elif isinstance(key, int):
            if key in self.year_index:
                return self.year_index[key] 
        raise KeyError(f"Ключ '{key}' не найден в словаре")
    def update_index(self,book):
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
            self.year_index[book.year] = []
        if book not in self.title_index[book.title]:
            self.title_index[book.title].append(book)
    def remove_book(self, book):
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
                self.year_index[book.title].remove(book)
                if not self.title_index[book.title]:
                    del self.title_index[book.title]
    def find_by_author(self, author: str):
        return self.author_index.get(author, [])   
    def find_by_year(self, year: int):
        return self.year_index.get(year, [])    
    def find_by_title(self, title: str):
        return self.title_index.get(title, [])
    def find_by_isbn(self, isbn: str):
        return self.isbn_index.get(isbn,[])

    