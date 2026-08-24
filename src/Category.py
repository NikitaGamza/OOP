from typing import List, Optional

from src.LawnGrass import LawnGrass
from src.Product import Product
from src.Smartphone import Smartphone
from src.ZeroProductError import ZeroProductError


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
        """Подсчет общего количества продуктов в категории продукта"""
        full_quantity_products = 0
        for product in self.__products:
            full_quantity_products += product.quantity
        return f"{self.name}, количество продуктов: {full_quantity_products} шт."

    def add_product(self, product: Product | LawnGrass | Smartphone) -> None:
        """Метод для добавления продукта в категорию."""
        if (
            isinstance(product, Product)
            | isinstance(product, LawnGrass)
            | isinstance(product, Smartphone)
        ):
            try:
                if product.quantity <= 0:
                    raise ZeroProductError
            except ZeroProductError as e:
                print(str(e))
            else:
                Category.product_count = Category.product_count + 1
                self.__products.append(product)
        else:
            raise TypeError("Добавляется только: Продукт, Газонная Трава, Смартфон")

    @property
    def products(self):
        """Геттер, выводящий список товаров в строковом виде"""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result
