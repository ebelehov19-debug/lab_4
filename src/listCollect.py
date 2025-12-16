class BookCollection:
    def __init__(self):
        self.books=[]
    def __len__(self) -> int:
        return len(self.books)
    def __iter__(self):
        return iter(self.books)
    def __getitem__(self, ind):
        return self.books[ind]
    def add(self,val)->None:
        self.books.append(val)
    def delite(self,book)->None:
        if book in self.books:
            self.books.remove(book)
    def __contains__(self, book):
        return book in self.books

        
    