from src.ClassPriceBook import PriceBook
def test_init():
    book = PriceBook("Книга", "Автор", 2023, "Жанр", "52", 1000.0, 5)
    assert book.title == "Книга"
    assert book.price == 1000.0
    assert book.quantity == 5
    assert book.total_sold == 0
    assert book.is_for_sale == True
def test_sell():
    book = PriceBook("Книга", "Автор", 2023, "Жанр", "1", 500.0, 10)
    result = book.sell(3)
    assert "Продано 3 книг 'Книга' за 1500.0 рублей" == result
    assert book.quantity == 7
    assert book.total_sold == 3
def test_sell_last_book():
    book = PriceBook("Книга", "Автор", 2023, "Жанр", "1", 500.0, 1)
    book.sell(1)
    assert book.quantity == 0
    assert book.is_for_sale == False
def test_sell_not():
    book = PriceBook("Книга", "Автор", 2023, "Жанр", "1", 500.0, 0)
    book.is_for_sale = False
    result = book.sell(1)
    assert "Книга 'Книга' не доступна для продажи" in result
    assert book.quantity == 0
def test_sell_more():
    book = PriceBook("Книга", "Автор", 2023, "Жанр", "1", 500.0, 1)
    result = book.sell(2)
    assert result == "Недостаточно книг 'Книга' в наличии 1"
    assert book.quantity == 1
def test_zakup():
    book = PriceBook("Книга", "Автор", 2023, "Жанр", "1", 500.0, 1)
    res = book.zakup(10)
    assert res == "Закуплено 10 книг 'Книга'. Теперь в наличии: 11"
    assert book.quantity == 11 
    assert book.price == 500.0  
    assert book.is_for_sale == True
def test_change_price_zak():
    book = PriceBook("Книга", "Автор", 2023, "Жанр", "1", 500.0, 1)
    res=book.zakup(10,520)
    assert res == "Новая цена: 520 рублей. Закуплено 10 книг 'Книга'. Теперь в наличии: 11"
    assert book.quantity ==11
    assert book.price == 520
def rest_change_price():
    book = PriceBook("Книга", "Автор", 2023, "Жанр", "1", 500.0, 1)
    res = book.change_price(520.0)
    assert res == "Новая цена 1500.0"
    assert book.price == 1500.0
def test_stat():
    book = PriceBook("Книга", "Автор", 2023, "Жанр", "ISBN-123", 1000.0, 10)
    book.sell(3)
    book.sell(2)
    stats = book.get_sales_statistics()
    assert stats['title'] == "Книга"
    assert stats['total_sold'] == 5
    assert stats['total_revenue'] == 5000.0
    assert stats['current_quantity'] == 5
    assert stats['is_for_sale'] == True



