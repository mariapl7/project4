from src.main import Product, Category


class ProductIterator:
    """Итератор для перебора продуктов в категории."""


def __init__(self, category_obj):
    self.category = category_obj
    self.index = 0


def __iter__(self):
    """Возвращает объект итератора (сам себя)."""
    return self


def __next__(self):
    """Возвращает следующий продукт из категории или вызывает StopIteration."""
    if self.index < len(self.category.products):
        products = self.category.products[self.index]
        self.index += 1
        return products
    raise StopIteration


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category("Смартфоны", "Современные смартфоны.", [product1, product2, product3])

    iterator = ProductIterator(category)

    for product in iterator:
        print(product)
