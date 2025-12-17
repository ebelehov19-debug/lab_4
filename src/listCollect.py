class BookCollection:
    def __init__(self):
        self.books=[]
    def __len__(self) -> int:
        return len(self.books)
    def __iter__(self):
        return iter(self.books)
    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.books[index.start:index.stop:index.step]
        if index < 0:
            index = len(self.books) + index
        if 0 <= index < len(self.books):
            return self.books[index]    
        raise IndexError(f"Индекс вне допустимого диапазона диапазона")
    def add(self,val)->None:
        self.books.append(val)
    def delite(self,book)->None:
        if book in self.books:
            self.books.remove(book)
    def __contains__(self, book):
        return book in self.books
    def __repr__(self):
        return f"BookCollection имеет {len(self.books)} книг"

        
    