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
def test_category(apple, banana):
    return Category('Фрукты', 'ЗОЖ', [apple, banana])


def category_fruit(test_category, apple, banana):
    assert test_category.name == 'Фрукты'
    assert test_category.description == 'ЗОЖ'
    assert test_category.products == [apple, banana]

@pytest.fixture()
def test_category_unique_item(test_category):
    assert test_category.cnt_category == 1
    assert test_category.cnt_unique_item == 2





