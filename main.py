from typing import List, Optional, Any


class Product:
    """Класс продукции"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

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
            return cls(parameters["name"], parameters["description"], parameters["price"], parameters["quantity"])


class Category:
    """Класс категорий продукта"""

    name: str
    description: str
    __products: List[Product]
    category_count: int = 0
    product_count = 0


    def __init__(
        self, name: str, description: str, products: Optional[List[Product]] = None
    ) -> None:
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count = Category.category_count + 1
        Category.product_count = Category.product_count + len(self.__products)

    def add_product(self, product: Product):
        """Метод для добавления продукта в категорию."""
        product.category = self  # Назначаем категорию продукту
        self.__products.append(product)

    @property
    def get_products(self):
        """Геттер, выводящий список товаров в строковом виде"""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

if __name__ == "__main__":
    prod1 = Product("Samsung", "256GB Blue", 200, 10)
    new_prod = prod1.new_product({"name": "LG", "description": "256GB Blue", "price": 300, "quantity": 5})
    print(new_prod.name)
    # def phone_list():
    #     phone1 = Product("Samsung", "256GB Blue", 200, 10)
    #     phone2 = Product("LG", "256GB Black", 150, 8)
    #     phone3 = Product("Xiaomi", "256GB Green", 250, 12)
    #     return [phone1, phone2, phone3]
    #
    # cat1 = Category("Телефоны", "Смартфоны и мобильные устройства", phone_list())
    #
    # print(cat1.product_count)
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
    # category2 = Category("Телевизоры",
    #                      "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    #                      [product4])
    #
    # print(category2.name)
    # print(category2.description)
    # # print(len(category2.products))
    # # print(category2.products)
    #
    # print(Category.category_count)
    # print(Category.product_count)
