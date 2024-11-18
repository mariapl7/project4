from src.base_product import BaseProduct
from src.print_mixin import PrintMixin
from src.exceptions import ZeroQuantityError


class Product(BaseProduct, PrintMixin):
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

        if quantity <= 0:  # Изменение условия: теперь проверяем на <= 0
            raise ValueError('Товар может быть добавлен только с положительным количеством.')
        self.quantity = quantity

        self.full_price = price * quantity  # Инициализация full_price
        Product.product_count += 1  # Увеличение счетчика продуктов
        super().__init__()


    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


    def __add__(self, other):
        if type(other) is Product:
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError("Нельзя складывать продукты разных классов.")


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
    products: list
    product_count = 0
    category_count = 0


    def __init__(self, name, description, products=None):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1


    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product):
        """Добавляет продукт в категорию."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников.")

        if product.quantity <= 0:
            raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен.")

        self.__products.append(product)
        print(f"Товар '{product.name}' добавлен в категорию '{self.name}'.")

    @property
    def products(self):
        return self.__products

    def average_price(self):
        try:
            if not self.__products:
                raise ValueError("Нет товаров в категории.")

            total_price = sum(product.price * product.quantity for product in self.__products)
            total_quantity = sum(product.quantity for product in self.__products)
            average = total_price / total_quantity
            return average
        except ValueError as e:
            print(e)
            return 0


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

    # product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, quantity=-1)

    # Создаем пустую категорию
    category = Category("Пустая категория", "Категория без продуктов", products=[])
    print(category.average_price())  # Вывод: 0, так как нет товаров

    # Добавляем продукты в категорию
    category.add_product(Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5))
    category.add_product(Product("Iphone 15", "512GB, Gray space", 210000.0, 8))
    category.add_product(Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14))

    print(category.average_price())

    try:
        category.add_product(product1)  # Успешное добавление
    except Exception as e:
        print(e)

    try:
        category.add_product(product2)  # Ошибка при добавлении
    except Exception as e:
        print(e)
