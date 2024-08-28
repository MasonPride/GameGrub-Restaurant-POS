"""CatanSkewers

This is a class that creates the CatanSkewers
side menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from typing import List, Set
from src.gamegrub.data.enums.Size import Size


class CatanSkewers:

    def __init__(self) -> None:
        self.__size: Size = Size.JUNIOR
        self.__price: float = 4.45
        self.__calories: int = 530

    @property
    def size(self) -> Size:
        return self.__size

    @size.setter
    def size(self, value: Size) -> None:
        self.__size = value
        if value == Size.CLASSIC:
            self.__price: float = 6.85
            self.__calories: int = 815
        elif value == Size.WINNER:
            self.__price = 8.65
            self.__calories = 1045
        else:
            self.__price: float = 4.45
            self.__calories: int = 530

    @property
    def price(self) -> float:
        return self.__price

    @property
    def calories(self) -> int:
        return self.__calories

    def __str__(self) -> str:
        return "{} Catan Skewers".format(self.__size)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, CatanSkewers):
            return (self.__size == value.size and
                    self.__price == value.price and
                    self.__calories == value.calories)
        else:
            return False
