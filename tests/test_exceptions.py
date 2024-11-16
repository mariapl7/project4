import pytest
from src.main import Product
from src.exceptions import ZeroQuantityError


def test_add_product_success(category, product):
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0] == product


def test_add_product_with_zero_quantity(category):
    product_with_zero_quantity = Product("Iphone 15", "512GB, Gray space", 210000.0, quantity=0)
    with pytest.raises(ZeroQuantityError):
        category.add_product(product_with_zero_quantity)


def test_average_price(category):
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, quantity=5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, quantity=8)
    category.add_product(product1)
    category.add_product(product2)
    assert category.average_price() == (900000.0 + 1680000.0) / 13  # (180000.0 * 5 + 210000.0 * 8) / 13

