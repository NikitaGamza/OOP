from main import Product, Category
import pytest


@pytest.fixture()
def product_phone():
    return Product("Samsung", "256GB Blue", 200, 10)


def test_product_phone__init(product_phone):
    assert product_phone.name == "Samsung"
    assert product_phone.description == "256GB Blue"
    assert product_phone.price == 200
    assert product_phone.quantity == 10
    new_prod = product_phone.new_product({"name": "LG", "description": "256GB Blue", "price": 300, "quantity": 5})
    assert new_prod.name == "LG"
    new_prod.price = 450
    assert new_prod.price == 450

def get_phone_list():
    phone1 = Product("Samsung", "256GB Blue", 200, 10)
    phone2 = Product("LG", "256GB Black", 150, 8)
    phone3 = Product("Xiaomi", "256GB Green", 250, 12)
    result = ""
    for product in [phone1, phone2, phone3]:
        result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
    return result

def phone_list():
    phone1 = Product("Samsung", "256GB Blue", 200, 10)
    phone2 = Product("LG", "256GB Black", 150, 8)
    phone3 = Product("Xiaomi", "256GB Green", 250, 12)
    return [phone1, phone2, phone3]

@pytest.fixture()
def category_phone():
    return Category("Телефоны", "Smartphones", "Смартфоны и мобильные устройства", phone_list())

def test_category_phone__init(category_phone):
    assert category_phone.name == "Телефоны"
    assert category_phone.description == "Смартфоны и мобильные устройства"
    assert category_phone.products == get_phone_list()
    assert category_phone.category_count == 1
    assert category_phone.product_count == 3