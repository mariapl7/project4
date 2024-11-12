import unittest
from src.main import Product, Category


def test_product_initialization():
    """Тестируем инициализацию продукта."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_str():
    """Тестируем строковое представление продукта."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_addition():
    """Тестируем сложение продуктов."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    total_price = product1 + product2
    assert total_price == (180000.0 * 5) + (210000.0 * 8)


def test_product_price_setter():
    """Тестируем установку цены продукта."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product.price = 180000.0
    assert product.price == 180000.0

    try:
        product.price = -80000.0
    except ValueError:
        assert True
    else:
        assert False, "Ожидалось исключение ValueError"


def test_category_initialization():
    """Тестируем инициализацию категории."""
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, "
                                     "но и получения дополнительных функций для удобства жизни", [])
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации, "
                                    "но и получения дополнительных функций для удобства жизни")
    assert category.products == []


def test_category_add_product():
    """Тестируем добавление продукта в категорию."""
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, "
                                     "но и получения дополнительных функций для удобства жизни", [])
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    category.add_product(product)
    assert product in category.products

    try:
        category.add_product("Некорректный продукт")
    except TypeError:
        assert True
    else:
        assert False, "Ожидалось исключение TypeError"


def test_category_str():
    """Тестируем строковое представление категории."""
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, "
                                     "но и получения дополнительных функций для удобства жизни", [])
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category.add_product(product1)
    category.add_product(product2)
    assert str(category) == "Смартфоны, количество продуктов: 13 шт."

if __name__ == "__main__":
    unittest.main()
