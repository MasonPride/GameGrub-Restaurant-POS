"""CandyLandShake class
This is a class that creates the Candy Land Shake
drink menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from typing import List, Set
from src.gamegrub.data.enums.Size import Size


class CandyLandShake:

    def __init__(self) -> None:
        self.__size: Size = Size.JUNIOR
        self.__price: float = 5.75
        self.__calories: int = 770
        self.__chocolate: bool = True
        self.__vanilla: bool = False
        self.__strawberry: bool = False
    
    @property
    def size(self) -> Size:
        return self.__size

    @size.setter
    def size(self, value: Size) -> None:
        self.__size = value
        if value == Size.CLASSIC:
            self.__price = 7.45
            self.__calories = 1215
        elif value == Size.WINNER:
            self.__price = 9.55
            self.__calories = 1465
        else:
            self.__price = 5.75
            self.__calories = 770

    @property
    def price(self) -> float:
        return self.__price

    @property
    def calories(self) -> int:
        return self.__calories

    @property
    def chocolate(self) -> bool:
        return self.__chocolate
    
    @chocolate.setter
    def chocolate(self, value: bool) -> None:
        self.__chocolate = value

    @property
    def vanilla(self) -> bool:
        return self.__vanilla
    
    @vanilla.setter
    def vanilla(self, value: bool) -> None:
        self.__vanilla = value

    @property
    def strawberry(self) -> bool:
        return self.__strawberry
    
    @strawberry.setter
    def strawberry(self, value: bool) -> None:
        self.__strawberry = value

    @property
    def instructions(self) -> List[str]:
        instruct: List[str] = []
        if not self.__chocolate:
            instruct.append("Hold Chocolate")
        if self.__vanilla:
            instruct.append("Add Vanilla")
        if self.__strawberry:
            instruct.append("Add Strawberry")
        return instruct.copy()

    def __str__(self) -> str:
        return "{} Candy Land Shake".format(self.__size)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, CandyLandShake):
            return (self.__size == value.size and
                    self.__price == value.price and
                    self.__calories == value.calories and
                    self.__chocolate == value.chocolate and
                    self.__vanilla == value.vanilla and
                    self.__strawberry == value.strawberry)
        else:
            return False
