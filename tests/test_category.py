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


def test_category(category_fruit, apple, banana):
    assert category_fruit.name == 'Фрукты'
    assert category_fruit.description == 'ЗОЖ'
    assert category_fruit.products == [apple, banana]

if __name__ == '__main__':
    cat_1 = Category('Фрукты', 'ЗОЖ', [apple, banana])
    cat_2 = Category('Овощи', 'ЗОЖ', [apple, banana])
    cat_3 = Category('Фрукты', 'ЗОЖ', [apple, banana])
print(f"Общее кол-во категорий: {Category.cnt_category}")
print(f"Общее кол-во уникальных продуктов: {Category.cnt_unique_item}")