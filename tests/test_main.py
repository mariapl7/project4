import unittest
from src.main import Product


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, "
                                          "но и получения дополнительных функций для удобства жизни")
    assert len(first_category.protucts) == 3

    assert second_category.name == "Телевизоры"
    assert len(second_category.products) == 1

    assert first_category.category_count == 2
    assert second_category.product_count == 4


def test_product_str(product1):
    assert str(product1) == '"Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5"'


def test_product_add(product1, product2):
    assert product1 + product2 == (18000.0 * 5) + (210000.0 * 8)


def test_category_str(category):
    assert str(category) == ('"Смартфоны, как средство не только коммуникации, '
                             'но и получения дополнительных функций для удобства жизни"), '
                             '[product1, product2, product3]"')


def test_category_add_product(category):
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category.add_product(product2)
    assert str(category) == ('"Смартфоны, как средство не только коммуникации, '
                             'но и получения дополнительных функций для удобства жизни", '
                             '[product1, product2, product3]"')


if __name__ == '__main__':
    unittest.main()
