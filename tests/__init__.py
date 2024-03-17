import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def apple():
    return Product('Яблоко', 'Антоновка', 50, 25)

@pytest.fixture
def banana():
    return Product('Банан', 'Эквадор импорт', 50.99, 12)

@pytest.fixture
def category_fruit(apple, banana):
    return Category('Фрукты', 'ЗОЖ', [apple, banana])


@pytest.fixture
def test_summ(category_fruit):
    assert category_fruit.cnt_category == 1
    assert category_fruit.cnt_unique_item == 2


if __name__ == '__main__':
    cat_1 = Category('Фрукты', 'ЗОЖ', [1, 2, 3, 4])
    cat_2 = Category('Овощи', 'ЗОЖ', [1, 2, 3, 4])
    cat_3 = Category('Фрукты', 'ЗОЖ', [1, 2, 3, 4])
print(f"Общее кол-во категорий: {Category.cnt_category}")
print(f"Общее кол-во уникальных продуктов: {Category.cnt_unique_item}")


@pytest.fixture
def test_category(category_fruit):
    assert category_fruit.name == 'Фрукты'
    assert category_fruit.description == 'ЗОЖ'
    assert category_fruit.products == [apple, banana]




