"""ChessChickenParm class

This is a class that creates the Chess Chicken Parm
menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from typing import List, Set
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings


class ChessChickenParm:

    def __init__(self) -> None:
        self.__base: Base = Base.SPAGHETTI
        self.__toppings: Set[Toppings] = {Toppings.CHEESE, Toppings.FRESH_HERBS}
        self.__price: float = 12.15
        self.__red_sauce: bool = True
        self.__crispy_chicken: bool = True

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
        return 1555

    @property
    def red_sauce(self) -> bool:
        return self.__red_sauce

    @red_sauce.setter
    def red_sauce(self, value: bool) -> None:
        self.__red_sauce = value

    @property
    def crispy_chicken(self) -> bool:
        return self.__crispy_chicken

    @crispy_chicken.setter
    def crispy_chicken(self, value: bool) -> None:
        self.__crispy_chicken = value

    @property
    def instructions(self) -> List[str]:
        ingredients: List[str] = []
        if not self.__red_sauce:
            ingredients.append("Hold Red Sauce")
        if not self.__crispy_chicken:
            ingredients.append("Hold Crispy Chicken")
        return ingredients.copy()

    def __str__(self) -> str:
        return "Chess Chicken Parm on {}".format(self.__base)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, ClueChili):
            return (self.__base == value.base and 
                    self.__toppings == value.toppings and
                    self.__red_sauce == value.red_sauce and
                    self.__crispy_chicken == value.crispy_chicken)
        else:
            return False
