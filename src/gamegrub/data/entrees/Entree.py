"""Entree Base class.

This class creates the abstract class for all
entrees

Author: Mason Pride
Version: 0.1
"""

from typing import List, Set
from src.gamegrub.data.Item import Item
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings


class Entree(Item):
    """Entree class.

    This class creates the abstract methods to
    be used by entree items.
    """

    def __init__(self) -> None:
        """Initialize class.

        Initializes the commmon attributes for
        entrees.
        """
        self.__base: Base = None
        self.__toppings: Set[Toppings] = set()

    @property
    def base(self) -> Base:
        """Base getter.

        Gets the base attribute of entree.

        Returns:
            Base attrbute of entree
        """
        return self.__base

    @base.setter
    def base(self, value: Base) -> None:
        """Base setter.

        Sets the base attribute of entree.
        """
        self.__base = value

    @property
    def toppings(self) -> Set[Toppings]:
        """Toppings attribute getter method.

        Gets the toppings attribute of the class.

        Returns:
            Shallow copy of toppings attribute
            of the object; a set containing the toppings
        """
        return self.__toppings.copy()

    def add_topping(self, value: Toppings) -> None:
        """Add toppings to object.

        Adds a topping from the Toppings enum class
        to the set of toppings of the object.

        Args:
            value: The desired topping from Toppings enum
        """
        self.__toppings.add(value)

    def remove_topping(self, value: Toppings) -> None:
        """Remove toppings from object.

        Removes a topping from the toppings set

        Args:
            value: The desired topping from Toppings enum
        """
        if value in self.__toppings:
            self.__toppings.discard(value)

    def instructions(self) -> List[str]:
        """Gets instructions.

        Helps construct instructions list.

        Returns:
            List of strings of instructions
        """
        # create list
        instructs: List[str] = list()
        # add all toppings to list as strings
        for topping in self.toppings:
            instructs.append(str(topping))
        # return list
        return instructs
