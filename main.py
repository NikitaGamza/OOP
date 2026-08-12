from typing import Any, List, Optional


class Product:
    """Класс продукции"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Возврат форматированной строки характеристик товара"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, parameters: dict, product_list: Any | None = None):
        if not product_list:
            product_list = []
        for existing_product in product_list:
            if existing_product.name == parameters["name"]:
                parameters["quantity"] += existing_product.quantity
                if existing_product.price > parameters["price"]:
                    parameters["price"] = existing_product.price
        else:
            return cls(
                parameters["name"],
                parameters["description"],
                parameters["price"],
                parameters["quantity"],
            )

    @property
    def price(self):
        """Геттер цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер новой цены"""
        if new_price > 0:
            if self.__price > new_price:
                select = ""
                print("Вы уверены, что хотите понизить цену? y - да, n - нет")
                while select != "Y" and select != "N":
                    select = input().upper()
                    if select != "Y" and select != "N":
                        print("Некорректный ввод")
                        print("Вы уверены, что хотите понизить цену? y - да, n - нет")
                if select == "Y":
                    self.__price = new_price
                elif select == "N":
                    self.__price = self.__price
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Smartphone(Product):
    """Класс смартфонов"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: int,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other) -> float | TypeError:
        if not isinstance(other, Smartphone):
            return TypeError('Общую сумму можно посчитать только с одних и тех же товаров')
        return self.__price * self.quantity + other.__price * other.quantity


class LawnGrass(Product):
    """Класс травы"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: int,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other) -> float | TypeError:
        if not isinstance(other, LawnGrass):
            return TypeError('Общую сумму можно посчитать только с одних и тех же товаров')
        return self.__price * self.quantity + other.__price * other.quantity

class Category:
    """Класс категорий продукта"""

    name: str
    category: str
    description: str
    __products: List[Product]
    category_count: int = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        category: str,
        description: str,
        products: Optional[List[Product]] = None,
    ) -> None:
        self.name = name
        self.category = category
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count = Category.category_count + 1
        Category.product_count = Category.product_count + len(self.__products)

    def __str__(self) -> str:
        # Подсчет общего количества продуктов в категории продукта
        full_quantity_products = 0
        for product in self.__products:
            full_quantity_products += product.quantity
        return f"{self.name}, количество продуктов: {full_quantity_products} шт."

    def add_product(self, product: Product):
        """Метод для добавления продукта в категорию."""
        Category.product_count = Category.product_count + 1
        self.__products.append(product)

    @property
    def products(self):
        """Геттер, выводящий список товаров в строковом виде"""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result


if __name__ == "__main__":
    prod1 = Product("Samsung", "256GB Blue", 200, 10)
    new_prod = prod1.new_product(
        {"name": "LG", "description": "256GB Blue", "price": 300, "quantity": 5}
    )
    print(new_prod)
    print(prod1 + new_prod)
    prod1.price = 450
    print(prod1.price)

    def phone_list():
        phone1 = Product("Samsung", "256GB Blue", 200, 10)
        phone2 = Product("LG", "256GB Black", 150, 8)
        phone3 = Product("Xiaomi", "256GB Green", 250, 12)
        return [phone1, phone2, phone3]

    #
    cat1 = Category(
        "Телефоны", "Смартфоны и мобильные устройства", "some description", phone_list()
    )
    cat1.add_product(prod1)
    print(cat1.product_count)
    # product1 = Product(
    #     "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    # )
    # product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    # product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    #
    # print(product1.name)
    # print(product1.description)
    # print(product1.price)
    # print(product1.quantity)
    #
    # print(product2.name)
    # print(product2.description)
    # print(product2.price)
    # print(product2.quantity)
    #
    # print(product3.name)
    # print(product3.description)
    # print(product3.price)
    # print(product3.quantity)
    #
    # category1 = Category(
    #     "Смартфоны",
    #     "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    #     [product1, product2, product3],
    # )
    #
    # print(category1.name == "Смартфоны")
    # print(category1.description)
    # # print(len(category1.products))
    # print(category1.category_count)
    # print(category1.product_count)
    # cat1 = Category("Спальня", "товары для сна", [product1, product2, product3])
    # print(cat1.category_count)
    # print(cat1.product_count)
    #
    # product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    #
    # print(category2.name)
    # print(category2.description)
    # # print(len(category2.products))
    # # print(category2.products)
    #
    # print(Category.category_count)
    # print(Category.product_count)
