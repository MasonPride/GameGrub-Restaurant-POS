"""JengaNachos class

This is a class that creates the Jenga Nachos
menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from typing import List, Set
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings


class JengaNachos:

    def __init__(self) -> None:
        self.__base: Base = Base.CHIPS
        self.__toppings: Set[Toppings] = {Toppings.ONIONS, Toppings.CHEESE, Toppings.SOUR_CREAM, Toppings.HOT_SAUCE, Toppings.GUACAMOLE}
        self.__price: float = 9.85
        self.__spicy_beef: bool = True
        self.__beans: bool = True

    @property
    def base(self) -> Base:
        return self.__base

    @base.setter
    def base(self, value: Base) -> None:
        self.__base = value

    @property
    def toppings(self) -> Set[Toppings]:
        return self.__toppings.copy()

    def add_topping(self, value: Toppings) -> None:
        self.__toppings.add(value)

    def remove_topping(self, value: Toppings) -> None:
        if value in self.__toppings:
            self.__toppings.remove(value)

    @property
    def price(self) -> float:
        return self.__price + self.__base.amount

    @property
    def calories(self) -> int:
        return 1470

    @property
    def spicy_beef(self) -> bool:
        return self.__spicy_beef

    @spicy_beef.setter
    def spicy_beef(self, value: bool) -> None:
        self.__spicy_beef = value

    @property
    def beans(self) -> bool:
        return self.__beans

    @beans.setter
    def beans(self, value: bool) -> None:
        self.__beans = value

    @property
    def instructions(self) -> List[str]:
        ingredients: List[str] = []
        if not self.__spicy_beef:
            ingredients.append("Hold Spicy Beef")
        if not self.__beans:
            ingredients.append("Hold Beans")
        return ingredients.copy()

    def __str__(self) -> str:
        return "Jenga Nachos on {}".format(self.__base)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, JengaNachos):
            return (self.__base == value.base and 
                    self.__toppings == value.toppings and
                    self.__spicy_beef == value.spicy_beef and 
                    self.__beans == value.beans)
        else:
            return False
