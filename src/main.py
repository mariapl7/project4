class Product:
    """Клаcc для продукта."""
    name: str
    description: str
    price: float
    quantity: int
    product_count = 0
    full_price: float

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


    def __add__(self, other):
        if type(other) is Product:
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError


    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            raise ValueError('Цена не должна быть нулевая или отрицательная')
        self.__price = new_price


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
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += 1


    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


    def add_product(self, product: Product):
        if not isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError("Можно добавлять только объекты класса SmartPhone или его наследников.")


    @property
    def products(self):
        return self.__products


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    product_sum = product1 + product2
    print(product_sum)

    category = Category("Смартфоны", "Современные смартфоны.")
    category.add_product(product1)
    category.add_product(product2)

    print("Продукты в категории:")
    for product in category.products:
        print(product)

    # Попробуем добавить продукт другого класса
    try:
        category.add_product("Некорректный продукт")  # должен вызвать TypeError
    except TypeError as e:
        print(e)
