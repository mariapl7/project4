class Product:
    """Клаcc для продукта."""
    name: str
    description: str
    price: float
    quantity: int
    product_count = 0

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        self.__price.append(new_price)
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')


class Category:
    """Класс для категории."""
    name: str
    description: str
    products: str
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += 1

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        products_list = ""
        for product in self.__products:
            products_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            return products_list


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, "
                         "но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, "
                         "станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

    new_product = Product.new_product("Sony WH-1000XM5", "Беспроводные наушники", 50000.0, 10)
    print(f"Создан новый продукт: {new_product.name}, Цена: {new_product.price}")
