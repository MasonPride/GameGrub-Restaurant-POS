"""CraniumCoffee class
This is a class that creates the Cranium Coffee
drink menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from typing import List, Set
from src.gamegrub.data.enums.Size import Size


class CraniumCoffee:

    def __init__(self) -> None:
        self.__size: Size = Size.JUNIOR
        self.__price: float = 4.35
        self.__calories: int = 380
        self.__milk: bool = True
        self.__caramel: bool = False
        self.__chocolate: bool = False
        self.__mint: bool = False

    @property
    def size(self) -> Size:
        return self.__size

    @size.setter
    def size(self, value: Size) -> None:
        self.__size = value
        if value == Size.CLASSIC:
            self.__price = 5.25
            self.__calories = 495
        elif value == Size.WINNER:
            self.__price = 6.00
            self.__calories = 585
        else:
            self.__price = 4.35
            self.__calories = 380

    @property
    def price(self) -> float:
        return self.__price

    @property
    def calories(self) -> int:
        return self.__calories

    @property
    def milk(self) -> bool:
        return self.__milk
    
    @milk.setter
    def milk(self, value: bool) -> None:
        self.__milk = value

    @property
    def caramel(self) -> bool:
        return self.__caramel
    
    @caramel.setter
    def caramel(self, value: bool) -> None:
        self.__caramel = value

    @property
    def chocolate(self) -> bool:
        return self.__chocolate
    
    @chocolate.setter
    def chocolate(self, value: bool) -> None:
        self.__chocolate = value

    @property
    def mint(self) -> bool:
        return self.__mint
    
    @mint.setter
    def mint(self, value: bool) -> None:
        self.__mint = value

    @property
    def instructions(self) -> List[str]:
        instruct: List[str] = []
        if not self.__milk:
            instruct.append("Hold Milk")
        if self.__caramel:
            instruct.append("Add Caramel")
        if self.__chocolate:
            instruct.append("Add Chocolate")
        if self.__mint:
            instruct.append("Add Mint")
        return instruct.copy()

    def __str__(self) -> str:
        return "{} Cranium Coffee".format(self.__size)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, CraniumCoffee):
            return (self.__size == value.size and
                    self.__price == value.price and
                    self.__calories == value.calories and
                    self.__milk == value.milk and
                    self.__caramel == value.caramel and
                    self.__chocolate == value.chocolate and
                    self.__mint == value.mint)
        else:
            return False
