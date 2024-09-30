"""Combo class.

Represents a combo meal consisiting
of an entree, side, and drink.

Author: Mason Pride
Version: 0.1
"""
from src.gamegrub.data.item import Item
from src.gamegrub.data.entrees.Entree import Entree
from src.gamegrub.data.sides.Sides import Side
from src.gamegrub.data.drinks.Drinks import Drinks


class Combo(Item):
    """Combo class."""

    _discount = .80

    @classmethod
    def set_discount(cls, new_d):
        cls._discount = new_d

    def __init__(self) -> None:
        """Constructor for combo class."""
        self.__name: str = None
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
        """Name attribute setter

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
        """Entree attribute setter

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
        """Side attribute setter

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
        """Drink attribute setter

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
