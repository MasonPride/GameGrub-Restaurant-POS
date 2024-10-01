"""Combo class.

Represents a combo meal consisiting
of an entree, side, and drink.

Author: Mason Pride
Version: 0.1
"""
from src.gamegrub.data.Item import Item
from src.gamegrub.data.entrees.Entree import Entree
from src.gamegrub.data.sides.Side import Side
from src.gamegrub.data.drinks.Drink import Drink
from typing import List


class Combo(Item):
    """Combo class."""

    _discount = .80

    @classmethod
    def set_discount(cls, value: float) -> None:
        """Setter for discount.

        Args:
            value: new discount being set
        """
        cls._discount = value

    @classmethod
    def get_discount(cls) -> float:
        """Getter for discount.

        Returns:
            float representing the discount
        """
        return cls._discount

    def __init__(self, name: str = None) -> None:
        """Constructor for combo class."""
        self.__name = name
        self.__entree: Entree = None
        self.__side: Side = None
        self.__drink: Drink = None

    @property
    def name(self) -> str:
        """Name attribute getter.

        Returns:
            string representing the name
        """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """Name attribute setter.

        Args:
            value: The string to be set
        """
        self.__name = value

    @property
    def entree(self) -> Entree:
        """Entree attribute getter.

        Returns:
            Entree object representing an entree
        """
        return self.__entree

    @entree.setter
    def entree(self, value: Entree) -> None:
        """Entree attribute setter.

        Args:
            value: The entree to be set
        """
        self.__entree = value

    @property
    def side(self) -> Side:
        """Side attribute getter.

        Returns:
            Side object representing a side
        """
        return self.__side

    @side.setter
    def side(self, value: Side) -> None:
        """Side attribute setter.

        Args:
            value: The side to be set
        """
        self.__side = value

    @property
    def drink(self) -> Drink:
        """Drink attribute getter.

        Returns:
            Drink object representing a drink
        """
        return self.__drink

    @drink.setter
    def drink(self, value: Drink) -> None:
        """Drink attribute setter.

        Args:
            value: The drink to be set
        """
        self.__drink = value

    def clear(self) -> None:
        """Clear method.

        This method will clear the
        attributes of the combo, setting
        them all to None.
        """
        self.__name = None
        self.__entree = None
        self.__side = None
        self.__drink = None

    @property
    def price(self) -> float:
        """Getter for price.

        Gets the price of the items in combo

        Returns:
            float representing the price of combo
        """
        total = 0.0
        if self.__entree is not None:
            total += self.__entree.price
        if self.__drink is not None:
            total += self.__drink.price
        if self.__side is not None:
            total += self.__side.price
        if (self.__entree is not None and
                self.__drink is not None and
                self.__side is not None):
            return total + (total * self.__class__.get_discount())
        else:
            return total

    @property
    def calories(self) -> int:
        """Getter for calories.

        Gets the calories of the items in combo

        Returns:
            int representing the calories of the combo
        """
        total = 0
        if self.__entree is not None:
            total += self.__entree.calories
        if self.__drink is not None:
            total += self.__drink.calories
        if self.__side is not None:
            total += self.__side.calories
        return total

    @property
    def instructions(self) -> List[str]:
        """Instructions getter.

        Gets the instructions for the combo.

        Returns:
            List[str] representing the instructions
        """
        instructs: List[str] = []
        if self.name is not None:
            instructs.append(self.name)
        else:
            instructs.append("Custom Combo")
        if (self.__entree is not None and
                self.__drink is not None and
                self.__side is not None):
            instructs.append("${} Discount Applied".format(
                     self.__class__.get_discount()))
        return instructs

    def __eq__(self, value: object) -> bool:
        """Equals overide method.

        Checks to see if two menu items are equal.

        Args:
            value: Object representing an combo item

        Returns:
            True if items are equal;
            False if not
        """
        if isinstance(value, Combo):
            return (self.__name == value.name and
                    self.__entree == value.entree and
                    self.__drink == value.drink and
                    self.__side == value.side)
        else:
            return False
