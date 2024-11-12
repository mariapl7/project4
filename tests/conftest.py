from src.main import Product, Category
from src.smartphone import SmartPhone
from src.lawngrass import LawnGrass


import pytest


@pytest.fixture
def product1():
    """Фикстура для создания объекта Product."""
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category1(product_fixture):
    """Фикстура для создания объекта Category с продуктом."""
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации,"
                                 "но и получения дополнительных функций для удобства жизни", products=[product_fixture])


@pytest.fixture
def product2():
    """Фикстура для создания другого объекта Product."""
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def smartphone1():
    return SmartPhone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый"
    )

@pytest.fixture
def smartphone2():
    return SmartPhone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space"
    )

@pytest.fixture
def smartphone3():
    return SmartPhone(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
        efficiency=90.3,
        model="Note 11",
        memory=1024,
        color="Синий"
    )


@pytest.fixture
def grass1():
    """Фикстура для создания объекта LawnGrass."""
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый"
    )


@pytest.fixture
def grass2():
    """Фикстура для создания другого объекта LawnGrass."""
    return LawnGrass(
        name="Газонная трава 2",
        description="Выносливая трава",
        price=450.0,
        quantity=15,
        country="США",
        germination_period="5 дней",
        color="Темно-зеленый"
    )
