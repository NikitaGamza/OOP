import pytest

from src.Category import Category
from src.LawnGrass import LawnGrass
from src.Product import Product
from src.Smartphone import Smartphone
from src.WrongClass import WrongClass
from src.BaseProduct import BaseProduct


@pytest.fixture
def concrete_instance(monkeypatch):
    # Clear the abstract methods so Python allows instantiation
    monkeypatch.setattr(BaseProduct, "__abstractmethods__", set())
    return BaseProduct()


def test_abstract_pass_method(concrete_instance):
    result_price = concrete_instance.price()
    assert result_price is None
    result_new_product = concrete_instance.new_product({}, [])
    assert result_new_product is None
    result_add = concrete_instance.__add__({})
    assert result_add is None
    result_add = concrete_instance.__str__()
    assert result_add is None


@pytest.fixture()
def product_phone():
    return Product("Samsung", "256GB Blue", 200, 10)


def test_product_phone__init(product_phone):
    # assert product_phone == "Product (Samsung, 256GB Blue, 200, 10)"
    assert product_phone.name == "Samsung"
    assert product_phone.description == "256GB Blue"
    assert product_phone.price == 200
    product_phone.price = 250
    assert product_phone.price == 250
    assert product_phone.quantity == 10
    new_prod = product_phone.new_product(
        {"name": "LG", "description": "256GB Blue", "price": 300, "quantity": 5}
    )
    assert new_prod.name == "LG"
    new_prod.description = "256GB Blue"
    new_prod.price = 450
    assert new_prod.price == 450
    assert str(new_prod) == "LG, 450 руб. Остаток: 5 шт."
    res = product_phone + new_prod
    assert res == 4750


@pytest.fixture()
def product_smartphone():
    return Smartphone("Samsung", "256GB Blue", 200, 10, 1600, "Galaxy A16", 265, "Blue")


def test_product_smartphone__init(product_smartphone):
    new_prod = product_smartphone.new_product(
        {
            "name": "LG",
            "description": "256GB Blue",
            "price": 300,
            "quantity": 5,
            "efficiency": 1700,
            "model": "Galaxy A32",
            "memory": 512,
            "color": "brown",
        }
    )
    assert new_prod.name == "LG"
    new_prod.price = 450
    assert new_prod.price == 450
    assert str(new_prod) == "LG, 450 руб. Остаток: 5 шт."
    res = product_smartphone + new_prod
    assert res == 4250


@pytest.fixture()
def product_grass():
    return LawnGrass("Samsung", "256GB Blue", 200, 10, "Russia", 14, "Green")


def test_product_grass__init(product_grass):
    new_prod = product_grass.new_product(
        {
            "name": "LG",
            "description": "256GB Blue",
            "price": 300,
            "quantity": 5,
            "country": "USA",
            "germination_period": 10,
            "color": "brown",
        }
    )
    assert new_prod.name == "LG"
    new_prod.price = 450
    assert new_prod.price == 450
    assert str(new_prod) == "LG, 450 руб. Остаток: 5 шт."
    res = product_grass + new_prod
    assert res == 4250


def get_phone_list():
    phone1 = Product("Samsung", "256GB Blue", 200, 10)
    phone2 = Product("LG", "256GB Black", 150, 8)
    phone3 = Product("Xiaomi", "256GB Green", 250, 12)
    result = ""
    for product in [phone1, phone2, phone3]:
        result += (
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        )
    return result


@pytest.fixture()
def err_func():
    return TypeError("Общую сумму можно посчитать только с одних и тех же товаров")


@pytest.fixture()
def err_add_product():
    return TypeError("Добавляется только: Продукт, Газонная Трава, Смартфон")


def test_type_error(err_func, product_smartphone, product_grass, category_phone):
    with pytest.raises(TypeError):
        other_grass = LawnGrass("Samsung", "256GB Blue", 200, 10, "Russia", 10, "Green")
        wrong_res = product_smartphone + other_grass
        assert wrong_res == err_func()
        other_phone = Smartphone(
            "Samsung", "256GB Blue", 200, 10, 1600, "Galaxy A16", 265, "Blue"
        )
        wrong_res = product_smartphone + other_phone
        assert wrong_res == err_func()
        wrong_prod = WrongClass(
            "Samsung",
            "256GB Blue",
            200,
            10,
        )
        assert category_phone.add_product(wrong_prod) == err_add_product()


def phone_list():
    phone1 = Product("Samsung", "256GB Blue", 200, 10)
    phone2 = Product("LG", "256GB Black", 150, 8)
    phone3 = Product("Xiaomi", "256GB Green", 250, 12)
    return [phone1, phone2, phone3]


@pytest.fixture()
def category_phone():
    return Category(
        "Телефоны", "Smartphones", "Смартфоны и мобильные устройства", phone_list()
    )


def test_category_phone__init(category_phone):
    assert category_phone.name == "Телефоны"
    assert category_phone.description == "Смартфоны и мобильные устройства"
    assert category_phone.products == get_phone_list()
    assert category_phone.category_count == 1
    assert category_phone.product_count == 3
    assert str(category_phone) == "Телефоны, количество продуктов: 30 шт."
    new_phone = Product("Sony", "512GB Blue", 200, 10)
    category_phone.add_product(new_phone)
    assert category_phone.product_count == 4
    assert str(category_phone) == "Телефоны, количество продуктов: 40 шт."
    expexted = f'Samsung, 200 руб. Остаток: 10 шт.\nLG, 150 руб. Остаток: 8 шт.\nXiaomi, 250 руб. Остаток: 12 шт.\nSony, 200 руб. Остаток: 10 шт.\n'
    assert category_phone.products == expexted
