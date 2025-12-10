class IndexDict:
    def __init__(self):
        self.isbn_index = {}
        self.author_index = {}
        self.year_index = {}
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
        elif isinstance(key, int):
            if key in self.year_index:
                return self.year_index[key] 
        raise KeyError(f"Ключ '{key}' не найден в индексе")
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

    