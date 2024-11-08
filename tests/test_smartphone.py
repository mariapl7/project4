def test_add_product_to_category(category, product3):
    # Убедимся, что оба продукта успешно добавлены
    assert len(category.products) == 2
    category.add_product(product3)
    assert len(category.products) == 3


def test_add_invalid_product_type(category):
    try:
        category.add_product("Некорректный продукт")
    except TypeError as e:
        assert str(e) == "Можно добавлять только объекты класса SmartPhone или его наследников."


def test_smartphone_addition(product1, product2):
    result = product1 + product2  # Проверяем, что сложение выполняется
    expected_result = (product1.price * product1.quantity) + (product2.price * product2.quantity)
    assert result == expected_result


def test_smartphone_addition_invalid_type(product1):
    try:
        product1 + "Некорректный продукт"
    except TypeError as e:
        assert str(e) == "Нельзя складывать продукты разных классов."
