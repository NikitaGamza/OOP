from typing import Any

from src.Product import Product


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
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if not isinstance(other, LawnGrass):
            raise TypeError(
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
                parameters["country"],
                parameters["germination_period"],
                parameters["color"],
            )
