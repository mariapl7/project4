from src.main import Product
from src.smartphone import SmartPhone
from src.lawngrass import LawnGrass


def test_print_mixin(capsys):
    Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    SmartPhone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5,
               95.5, "S23 Ultra",256, "Серый")
    message = capsys.readouterr()
    message.out.strip() == "SmartPhone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия",
              "7 дней", "Зеленый")
    message = capsys.readouterr()
    message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"