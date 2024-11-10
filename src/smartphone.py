from src.main import Product


class SmartPhone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


    # def __add__(self, other):
    #     if type(other) is SmartPhone:
    #         return (self.price * self.quantity) + (other.price * other.quantity)
    #     raise TypeError("Нельзя складывать продукты разных классов.")


    def __add__(self, other):
        if not isinstance(other, SmartPhone):
            raise TypeError("Нельзя складывать продукты разных классов.")
        return (self.price * self.quantity) + (other.price * other.quantity)


if __name__ == "__main__":
    product1 = SmartPhone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra",
                          256, "Серый")
    product2 = SmartPhone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    product3 = SmartPhone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)
    print(product1.efficiency)
    print(product1.model)
    print(product1.memory)
    print(product1.color)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)
    print(product2.efficiency)
    print(product2.model)
    print(product2.memory)
    print(product2.color)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)
    print(product3.efficiency)
    print(product3.model)
    print(product3.memory)
    print(product3.color)

for product in Product:
    print(f"{product.name}: {product.description}, {product.price} руб., Остаток: {product.quantity} шт., "
          f"Эффективность: {product.efficiency}, Модель: {product.model}, Память: {product.memory} ГБ, "
          f"Цвет: {product.color}"
          )
