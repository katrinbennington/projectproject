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
def test_category():
    return Category('Фрукты', 'ЗОЖ', [apple, banana], 1, 2)


def category_fruit(test_category, apple, banana):
    assert test_category.name == 'Фрукты'
    assert test_category.description == 'ЗОЖ'
    assert test_category.products == [apple, banana]
    assert test_category.cnt_category == 1
    assert test_category.cnt_unique_item == 2

# @pytest.fixture()
# def test_category_unique_item(test_category):
#     assert test_category.cnt_category == 1
#     assert test_category.cnt_unique_item == 2

if __name__ == '__main__':
    cat_1 = Category('Фрукты', 'ЗОЖ', [apple, banana])
    cat_2 = Category('Овощи', 'ЗОЖ', [apple, banana])
    cat_3 = Category('Фрукты', 'ЗОЖ', [apple, banana])
print(f"Общее кол-во категорий: {Category.cnt_category}")
print(f"Общее кол-во уникальных продуктов: {Category.cnt_unique_item}")



