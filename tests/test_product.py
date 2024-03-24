import pytest
from src.product import Product


@pytest.fixture()
def product_apple():
    return Product('Яблоко', 'Антоновка', 50.00, 25)


def test_product(product_apple):
    assert product_apple.name == 'Яблоко'
    assert product_apple.description == 'Антоновка'
    assert product_apple._price == 50.00
    assert product_apple.quantity == 25


