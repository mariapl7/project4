import pytest


from src.main import Product, Category
from src.smartphone import SmartPhone


@pytest.fixture
def first_category():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                 5),
         Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
         Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)]
    )


@pytest.fixture
def second_category():
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        [Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)]
    )


@pytest.fixture
def product1():
    return Product("Товар1", "Описание товара 1", 100.0, 10)


@pytest.fixture
def product2():
    return Product("Товар2", "Описание товара 2", 200.0, 5)


@pytest.fixture
def category(product1):
    c = Category("Категория1", "Описание категории 1")
    c.add_product(product1)
    return c


@pytest.fixture
def product1():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category(product1, product2, product3):
    return Category("Смартфоны", "Современные смартфоны.", [product1, product2, product3])


@pytest.fixture
def product1():
    return SmartPhone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")

@pytest.fixture
def product2():
    return SmartPhone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

@pytest.fixture
def product3():
    return SmartPhone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

@pytest.fixture
def category(product1, product2):
    category = Category("Смартфоны", "Современные смартфоны")
    category.add_product(product1)
    category.add_product(product2)
    return category


import pytest
from src.lawngrass import LawnGrass

@pytest.fixture
def lawn_grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

@pytest.fixture
def lawn_grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
