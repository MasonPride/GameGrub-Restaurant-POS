"""YahtzeePoke class

This is a class that creates the Yahtzee Poke
menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from typing import List, Set
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings


class YahtzeePoke:

    def __init__(self) -> None:
        self.__base: Base = Base.RICE
        self.__toppings: Set[Toppings] = {Toppings.GUACAMOLE, Toppings.SOY_SAUCE, Toppings.HOT_SAUCE, Toppings.CRISPY_STRIPS}
        self.__price: float = 14.25
        self.__tuna: bool = True
        self.__veggies: bool = True
        self.__seaweed: bool = True

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
        return 785

    @property
    def tuna(self) -> bool:
        return self.__tuna

    @tuna.setter
    def tuna(self, value: bool) -> None:
        self.__tuna = value

    @property
    def veggies(self) -> bool:
        return self.__veggies

    @veggies.setter
    def veggies(self, value: bool) -> None:
        self.__veggies = value

    @property
    def seaweed(self) -> bool:
        return self.__seaweed

    @seaweed.setter
    def seaweed(self, value: bool) -> None:
        self.__seaweed = value
    
    @property
    def instructions(self) -> List[str]:
        ingredients: List[str] = []
        if not self.__tuna:
            ingredients.append("Hold Tuna")
        if not self.__veggies:
            ingredients.append("Hold Veggies")
        if not self.__seaweed:
            ingredients.append("Hold Seaweed")
        return ingredients.copy()

    def __str__(self) -> str:
        return "Yahtzee Poke on {}".format(self.__base)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, YahtzeePoke):
            return (self.__base == value.base and 
                    self.__toppings == value.toppings and
                    self.__tuna == value.tuna and 
                    self.__veggies == value.veggies and 
                    self.__seaweed == value.seaweed)
        else:
            return False

