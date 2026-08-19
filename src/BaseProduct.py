from abc import ABC, abstractmethod

from typing import Any


class BaseProduct(ABC):
    """Базовый абстрактный класс продукции"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other) -> float:
        pass

    @abstractmethod
    def new_product(self, parameters: dict, product_list: Any | None = None):
        pass

    @abstractmethod
    def price(self):
        pass
