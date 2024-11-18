from src.product_iterator import ProductIterator


def test_product_iterator(category_with_products):
    iterator = ProductIterator(category_with_products)
    products = list(iterator)

    assert len(products) == 3
    assert products[0].name == "Samsung Galaxy C23 Ultra"
    assert products[1].name == "Iphone 15"
    assert products[2].name == "Xiaomi Redmi Note 11"


def test_empty_category(empty_category):
    iterator = ProductIterator(empty_category)
    products = list(iterator)  # Преобразуем итератор в список

    assert len(products) == 0  # Проверяем, что список пустой

