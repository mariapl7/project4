import unittest
from src.main import Product, Category


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, "
                                          "но и получения дополнительных функций для удобства жизни")
    assert len(first_category.protucts) == 3

    assert second_category.name == "Телевизоры"
    assert len(second_category.products) == 1

    assert first_category.category_count == 2
    assert second_category.product_count == 4


def test_new_product_class_method():
    """Проверка работы класса new_product."""
    new_product = Product.new_product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert new_product.name == "Iphone 15", "Название продукта неверное"
    assert new_product.description == "512GB, Gray space", "Описание продукта неверное"
    assert new_product.price == 210000.0, "Цена продукта неверная"
    assert new_product.quantity == 8, "Количество продукта неверное"


def test_price_property(self):
    """Проверка работы свойства price."""
    assert self.product1.price == 180000.0, "Начальная цена продукта неверная"


def test_price_setter(self):
    """Проверка установки корректного значения цены."""
    self.product1.price = 200000.0
    assert self.product1.price == 200000.0, "Обновленная цена продукта неверная"


def test_add_product(self):
    """Проверка добавления продукта в категорию."""
    initial_count = Category.product_count
    self.category.add_product(self.product1)
    self.category.add_product(self.product2)

    # Проверяем, что количество продуктов в категории увеличилось
    assert len(self.category._Category__products) == 2, "Количество продуктов в категории неверное"
    assert Category.product_count == initial_count + 2, "Общее количество продуктов неверное"


def test_products_property(self):
    """Проверка свойства products."""
    self.category.add_product(self.product1)
    self.category.add_product(self.product2)

    expected_output = (
        "Samsung Galaxy C23 Ultra, 180000.0 руб.\nОстаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб.\nОстаток: 8 шт."
    ).strip()

    assert self.category.products == expected_output, "Список продуктов сформирован неверно"


if __name__ == '__main__':
    unittest.main()
