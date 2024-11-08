def test_lawn_grass_properties(grass1):
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_lawn_grass_addition(grass1, grass2):
    result = grass1 + grass2
    expected_result = (grass1.price * grass1.quantity) + (grass2.price * grass2.quantity)
    assert result == expected_result


def test_lawn_grass_addition_invalid_type(grass1):
    try:
        grass1 + "Некорректный продукт"  # Попытка сложить LawnGrass с строкой
    except TypeError as e:
        assert str(e) == "Нельзя складывать продукты разных классов."
    else:
        assert False, "Ожидалось исключение TypeError, но оно не было вызвано."
