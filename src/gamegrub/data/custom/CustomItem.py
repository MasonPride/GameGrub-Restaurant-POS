"""Custom Item class.

Creates a custom Item.

Author: Mason Pride
Version: 0.1
"""
from src.gamegrub.data.Item import Item
from typing import List


class CustomItem(Item):
    """Custom Item class."""

    def __init__(self, name: str = None,
                 price: float = None,
                 calories: int = None) -> None:
        """Constructor for the class."""
        self.__name = name
        self.__price = price
        self.__calories = calories

    @property
    def name(self) -> str:
        """Getter method for name."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """Setter method for name."""
        self.__name = value

    @property
    def price(self) -> float:
        """Getter method for price."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Setter method for price."""
        self.__price = value

    @property
    def calories(self) -> int:
        """Getter method for calories."""
        return self.__calories

    @calories.setter
    def calories(self, value: int) -> None:
        """Setter method for calories."""
        self.__calories = value

    @property
    def instructions(self) -> List[str]:
        """Instructions getter."""
        return list()
