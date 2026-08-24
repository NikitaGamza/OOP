from typing import Any

from src.BaseProduct import BaseProduct
from src.MixinRepr import MixinRepr


class Product(MixinRepr, BaseProduct):
    """Класс продукции"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()
        MixinRepr.__init__(self)

    def __str__(self) -> str:
        """Возврат форматированной строки характеристик товара"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        """Суммирование цен товаров"""
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
