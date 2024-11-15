import pytest
from src.exceptions import ZeroQuantityError


def test_add_product_success(category, product_with_positive_quantity):
    """Тест успешного добавления продукта в категорию."""
    category.add_product(product_with_positive_quantity)
    assert len(category.products) == 1
    assert category.products[0].name == "Samsung Galaxy S23 Ultra"


def test_add_product_zero_quantity(category, product_with_zero_quantity):
    """Тест добавления продукта с нулевым количеством."""
    with pytest.raises(ZeroQuantityError):
        category.add_product(product_with_zero_quantity)


def test_add_product_invalid_type(category):
    """Тест добавления продукта неверного типа."""
    with pytest.raises(TypeError):
        category.add_product("Некорректный продукт")  # Строка вместо объекта Product
