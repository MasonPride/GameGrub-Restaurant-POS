"""SorrySoda class
This is a class that creates the Sorry Soda
drink menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from typing import List, Set
from src.gamegrub.data.enums.Size import Size


class SorrySoda:

    def __init__(self) -> None:
        self.__size: Size = Size.JUNIOR
        self.__price: float = 2.55
        self.__calories: int = 370
        self.__cola: bool = True
        self.__cherry: bool = False
        self.__grape: bool = False
        self.__orange: bool = False

    @property
    def size(self) -> Size:
        return self.__size

    @size.setter
    def size(self, value: Size) -> None:
        self.__size = value
        if value == Size.CLASSIC:
            self.__price = 3.85
            self.__calories = 535
        elif value == Size.WINNER:
            self.__price = 5.35
            self.__calories = 765
        else:
            self.__price = 2.55
            self.__calories = 370

    @property
    def price(self) -> float:
        return self.__price

    @property
    def calories(self) -> int:
        return self.__calories

    @property
    def cola(self) -> bool:
        return self.__cola
    
    @cola.setter
    def cola(self, value: bool) -> None:
        self.__cola = value

    @property
    def cherry(self) -> bool:
        return self.__cherry
    
    @cherry.setter
    def cherry(self, value: bool) -> None:
        self.__cherry = value

    @property
    def grape(self) -> bool:
        return self.__grape
    
    @grape.setter
    def grape(self, value: bool) -> None:
        self.__grape = value

    @property
    def orange(self) -> bool:
        return self.__orange
    
    @orange.setter
    def orange(self, value: bool) -> None:
        self.__orange = value

    @property
    def instructions(self) -> List[str]:
        instruct: List[str] = []
        if not self.__cola:
            instruct.append("Hold Cola")
        if self.__cherry:
            instruct.append("Add Cherry")
        if self.__grape:
            instruct.append("Add Grape")
        if self.__orange:
            instruct.append("Add Orange")
        return instruct.copy()

    def __str__(self) -> str:
        return "{} Sorry Soda".format(self.__size)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, SorrySoda):
            return (self.__size == value.size and
                    self.__price == value.price and
                    self.__calories == value.calories and
                    self.__cola == value.cola and
                    self.__cherry == value.cherry and
                    self.__grape == value.grape and
                    self.__orange == value.orange)
        else:
            return False
