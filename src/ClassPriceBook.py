from src.classBook import Book

class PriceBook(Book):
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, price: float = 0.0, quantity: int = 1):
        """Создает книгу с ценой и количеством для продажи"""
        super().__init__(title, author, year, genre, isbn)
        self.price = price
        self.quantity = quantity
        self.total_sold = 0  
        self.total_revenue = 0.0  
        self.is_for_sale = True  
    def sell(self, cnt: int = 1) -> str:
        """Продает указанное количество книг"""
        if not self.is_for_sale:
            return f"Книга '{self.title}' не доступна для продажи"
        if cnt <= 0:
            return "Количество должно быть больше 0"
        if self.quantity < cnt:
            return f"Недостаточно книг '{self.title}' в наличии {self.quantity}"
        self.quantity -= cnt
        self.total_sold += cnt
        self.total_revenue += cnt * self.price
        if self.quantity == 0:
            self.is_for_sale = False
        return f"Продано {cnt} книг '{self.title}' за {cnt * self.price} рублей" 
    def zakup(self, quantity: int, new_price: float = None) -> str:
        """Закупает новые экземпляры книги"""
        if quantity <= 0:
            return "Количество должно быть больше 0"
        if new_price is not None and new_price > 0:
            self.price = new_price
        self.quantity += quantity
        self.is_for_sale = True  
        s = ''
        if new_price is not None and new_price > 0:
            s += f"Новая цена: {self.price} рублей. "
        return s + f"Закуплено {quantity} книг '{self.title}'. Теперь в наличии: {self.quantity}"
    def change_price(self, newprice: float) -> str:
        """Изменяет цену книги"""
        self.price = newprice
        return f"Новая цена {newprice}"
    def get_sales_statistics(self) -> dict:
        """Возвращает статистику продаж книги"""
        return {
            'title': self.title,
            'total_sold': self.total_sold,
            'total_revenue': self.total_revenue,
            'current_price': self.price,
            'current_quantity': self.quantity,
            'is_for_sale': self.is_for_sale,
        }