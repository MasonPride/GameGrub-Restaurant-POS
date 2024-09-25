"""Entree Base class.

This class creates the abstract class for all
entrees

Author: Mason Pride
Version: 0.1
"""

from typing import List, Set
from src.gamegrub.data.Item import Item
from src.gamegrub.data.enums.Base import Base


class Entree(Item):
    """Entree class.

    This class creates the abstract methods to
    be used by entree items.
    """

    def __init__(self) -> None:
        """initialize class.

        initializes the commmon attributes for 
        entrees.
        """
        self.__base: Base = Base.SPAGHETTI
        self.__toppings: Set[Toppings] = {}

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
