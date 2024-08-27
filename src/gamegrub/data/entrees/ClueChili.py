from typing import List, Set
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Size import Size
from src.gamegrub.data.enums.Toppings import Toppings


class ClueChili:

    def __init__(self) -> None:
        self.__base: Base = Base.SPAGHETTI
        self.__toppings: Set[Toppings] = {Toppings.ONIONS, Toppings.CHEESE, Toppings.HOT_SAUCE}
        self.__spicy_beef: bool = True
        self.__chili: bool = True
        self.__red_sauce: bool = True
        self.__beans: bool = True

    @property
    def base(self) -> Base:
        return self.__base

    @base.setter
    def base(self, value: Base) -> None:
        self.__base = value

    @property
    def toppings(self) -> Toppings:
        return self.__toppings.copy()

    def add_topping(self, value: Toppings) -> None:
        self.__toppings.add(value)

    def remove_topping(self, value: Toppings) -> None:
        self.__toppings.remove(value)

    @property
    def price(self) -> float:
        return 10.45

    @property
    def calories(self) -> int:
        return 1165

    @property
    def spicy_beef(self) -> bool:
        return self.__spicy_beef

    @spicy_beef.setter
    def spicy_beef(self, value: bool) -> None:
        self.__spicy_beef = value

    @property
    def chili(self) -> bool:
        return self.__chili

    @chili.setter
    def chili(self, value: bool) -> None:
        self.__chili = value

    @property
    def red_sauce(self) -> bool:
        return self.__red_sauce

    @red_sauce.setter
    def red_sauce(self, value: bool) -> None:
        self.__red_sauce = value

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
        if not self.__chili:
            ingredients.append("Hold Chili")
        if not self.__red_sauce:
            ingredients.append("Hold Red Sauce")
        if not self.__beans:
            ingredients.append("Hold Beans")
        return ingredients.copy()

    def __str__(self) -> str:
        return "Clue Chili on {}".format(self.__base)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, ClueChili):
            return (self.__base == value.base and 
                    self.__toppings == value.toppings and
                    self.__spicy_beef == value.spicy_beef and 
                    self.__chili == value.chili and 
                    self.__red_sauce == value.red_sauce and
                    self.__beans == value.beans)
        else:
            return False
