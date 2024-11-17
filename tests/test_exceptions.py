import pytest
from src.main import Product, Category
from src.exceptions import ZeroQuantityError


def test_add_product_success(category, product):
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0] == product


def test_create_product_with_zero_quantity():
    with pytest.raises(ValueError, match="Товар может быть добавлен только с положительным количеством."):
        Product(name="Zero Quantity Product", description="Product with zero quantity", price=100.0, quantity=0)


def test_add_product_to_category_with_negative_quantity():
    category = Category(name="Тестовая категория", description="Описание категории")
    with pytest.raises(ValueError, match="Товар может быть добавлен только с положительным количеством."):
        Product(name="Negative Quantity Product", description="", price=100.0, quantity=-5)


def test_average_price(category):
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, quantity=5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, quantity=8)
    category.add_product(product1)
    category.add_product(product2)
    assert category.average_price() == (900000.0 + 1680000.0) / 13  # (180000.0 * 5 + 210000.0 * 8) / 13


def test_average_price(category_with_products):
    expected_average = (180000.0 * 5 + 210000.0 * 8 + 31000.0 * 14) / (5 + 8 + 14)
    assert category_with_products.average_price() == expected_average