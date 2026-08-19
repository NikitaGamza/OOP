from src.Product import Product
from typing import Any


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

    def __add__(self, other):
        if not isinstance(other, Smartphone):
            return TypeError(
                "Общую сумму можно посчитать только с одних и тех же товаров"
            )
        return self.price * self.quantity + other.price * other.quantity

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
                parameters["efficiency"],
                parameters["model"],
                parameters["memory"],
                parameters["color"],
            )