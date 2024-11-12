import pytest


def test_smartphone_initialization(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_smartphone_addition(smartphone1):
    # Проверяем, что сложение с самим собой работает правильно
    result = smartphone1 + smartphone1
    expected_result = (smartphone1.price * smartphone1.quantity) * 2  # Умножаем на 2
    assert result == expected_result


def test_smartphone_addition_invalid_type(smartphone1):
    # Проверяем, что сложение с объектом другого типа вызывает ошибку
    with pytest.raises(TypeError, match="Нельзя складывать продукты разных классов."):
        smartphone1 + "not_a_smartphone"  # Попытка сложить с строкой

def test_smartphone_list(smartphone1, smartphone2, smartphone3):
    products = [smartphone1, smartphone2, smartphone3]
    assert len(products) == 3
    assert products[0].name == "Samsung Galaxy S23 Ultra"
    assert products[1].name == "Iphone 15"
    assert products[2].name == "Xiaomi Redmi Note 11"
