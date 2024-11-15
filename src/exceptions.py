class ZeroQuantityError(Exception):
    """Исключение, возникающее при попытке добавить товар с нулевым количеством."""
    def __init__(self, message="Товар с нулевым количеством не может быть добавлен."):
        self.message = message
        super().__init__(self.message)


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        try:
            if product.quantity <= 0:
                raise ZeroQuantityError()
            self.products.append(product)
        except ZeroQuantityError as e:
            print(e)
        else:
            print(f"Товар '{product.name}' добавлен в категорию '{self.name}'.")
        finally:
            print("Обработка добавления товара завершена.")


# Пример использования
if __name__ == '__main__':
    category = Category("Смартфоны")

    product1 = Product("Samsung Galaxy S23 Ultra", 180000.0, 5)
    product2 = Product("Iphone 15", 210000.0, 0)  # Товар с нулевым количеством

    category.add_product(product1)  # Успешное добавление
    category.add_product(product2)  # Ошибка при добавлении