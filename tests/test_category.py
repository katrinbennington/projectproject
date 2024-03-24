import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def apple():
    return Product('Яблоко', 'Антоновка', 50, 25)


@pytest.fixture
def banana():
    return Product('Банан', 'Эквадор импорт', 50.99, 25)


@pytest.fixture()
def category_fruit(apple, banana):
    return Category('Фрукты', 'ЗОЖ', [apple, banana])


@pytest.fixture()
def products_str():
    return Product('Яблоко', "Антоновка", 50.00, 25)


def test_category(category_fruit):
    assert category_fruit.name == 'Фрукты'
    assert category_fruit.description == 'ЗОЖ'
    assert category_fruit.products == 'Яблоко, 50 руб. Остаток: 25 шт.\nБанан, 50.99 руб. Остаток: 25 шт.\n'
    assert category_fruit.cnt_category == 1
    assert category_fruit.cnt_unique_item == 2
