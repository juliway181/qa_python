from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


import pytest

@pytest.fixture
def books_collector(self):
    books_collector = BooksCollector()
    return books_collector

#1
@pytest.mark.parametrize('book_name', ['Мастер и Маргарита', 'Гарри Поттер'])
def test_add_new_book(self, books_collector, book_name):
    books_collector.add_new_book(book_name)
    assert book_name in books_collector.get_books_genre()


#2
def test_add_dublicate_book(self, books_collector):
    book_name = '1984'
    books_collector.add_new_book(book_name)
    books_collector.add_new_book(book_name)
    assert len(books_collector.get_books_genre()) == 1


#3
def test_add_book_with_invalid_name(self, books_collector):
    books_collector.add_new_book('')
    books_collector.add_new_book('A' * 41)
    assert len(books_collector.get_books_genre()) == 0


#4
@pytest.mark.parametrize('book_name, genre', [
    ('Мастер и Маргарита','Фантастика'),
    ('Дракула','Ужасы')])

def test_set_book_genre_true(self, books_collector, book_name, genre):
    books_collector.add_new_book(book_name)
    books_collector.set_book_genre(book_name, genre)
    assert books_collector.get_book_genre(book_name) == genre


#5
def test_get_books_with_specific_genre_true(self, books_collector):
    books_collector.add_new_book('Книга 1')
    books_collector.add_new_book('Книга 2')
    books_collector.set_book_genre('Книга 1','Фантастика')
    books_collector.set_book_genre('Книга 2','Ужасы')
    assert books_collector.get_books_with_specific_genre('Фантастика') == ['Книга 1']


#6
def test_get_books_for_children_true(self, books_collector):
    books_collector.add_new_book('Книга 1')
    books_collector.add_new_book('Книга 2')
    books_collector.set_book_genre('Книга 1','Фантастика')
    books_collector.set_book_genre('Книга 2', 'Ужасы')
    assert books_collector.get_books_for_children() == ['Книга 1']


#7
def test_add_book_in_favourites_true(self, books_collector):
    book_name = 'Мастер и Маргарита'
    books_collector.add_new_book(book_name)
    books_collector.add_book_in_favorites(book_name)
    assert book_name in books_collector.get_list_of_favorites_books()


#8
def test_delete_book_from_favourites_true(self, books_collector):
    book_name = 'Мастер и Маргарита'
    books_collector.add_new_book(book_name)
    books_collector.add_book_in_favorites(book_name)
    books_collector.delete_book_from_favorites(book_name)
    assert book_name not in books_collector.get_list_of_favorites_books()


#9
def test_set_book_genre_non_existing_book(self, books_collector):
    books_collector.set_book_genre('Неизвестная книга', 'Фантастика')
    assert books_collector.get_book_genre('Неизвестная книга') == None


#10
def test_delete_existing_book_from_favourites(self, books_collector):
    book_name = 'Мастер и Маргарита'
    books_collector.add_new_book(book_name)
    books_collector.add_book_in_favorites(book_name)
    books_collector.delete_book_from_favorites('')
    assert book_name in books_collector.get_list_of_favorites_books()




