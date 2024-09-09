"""ChessChickenParm class.

This is a class that creates the Chess Chicken Parm
menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
from typing import List, Set
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings


class ChessChickenParm:
    """Represents the Chess Chicken Parm entree.

    This class builds the ChessChickenParm entree
    menu item.
    """

    def __init__(self) -> None:
        """Initializes the class.

        Creates the ChessChickenParm object with
        preset price, calories, base, toppings,
        and ingredients.
        """
        self.__base: Base = Base.SPAGHETTI
        self.__toppings: Set[Toppings] = {
            Toppings.CHEESE, Toppings.FRESH_HERBS}
        self.__price: float = 12.15
        self.__red_sauce: bool = True
        self.__crispy_chicken: bool = True

    @property
    def base(self) -> Base:
        """Base attribute getter method.

        Gets the base attribute of the class.

        Returns:
            base attribute of the class; of type Base
        """
        return self.__base

    @base.setter
    def base(self, value: Base) -> None:
        """Base attribute setter method.

        Sets the base, price, and calories
        attribute of the class to the desired Size.

        Args:
            value: The desired base from Base enum class
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
            self.__toppings.remove(value)

    @property
    def price(self) -> float:
        """Price attribute getter method.

        Gets the total price attribute of the class
        by adding the default price and base price

        Returns:
            price attribute of the object; of type float
        """
        return self.__price + self.__base.amount

    @property
    def calories(self) -> int:
        """Calories attribute getter method.

        Gets the calories attribute of the class.

        Returns:
            calories attribute of the object; of type int
        """
        return 1555

    @property
    def red_sauce(self) -> bool:
        """Red Sauce attribute getter method.

        Gets the red sauce attribute of the class.

        Returns:
            True if the entree has red sauce;
            False if not
        """
        return self.__red_sauce

    @red_sauce.setter
    def red_sauce(self, value: bool) -> None:
        """Red Sauce attribute setter method.

        Sets the red sauce attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing ingredient
            setting
        """
        self.__red_sauce = value

    @property
    def crispy_chicken(self) -> bool:
        """Crispy Chicken attribute getter method.

        Gets the crispy chicken attribute of the class.

        Returns:
            True if the entree has crispy chicken;
            False if not
        """
        return self.__crispy_chicken

    @crispy_chicken.setter
    def crispy_chicken(self, value: bool) -> None:
        """Crispy Chicken attribute setter method.

        Sets the crispy chicken attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing ingredient
            setting
        """
        self.__crispy_chicken = value

    @property
    def instructions(self) -> List[str]:
        """Shows the list of instructions.

        This method will return a list of the
        special instructions given to the entree.

        Returns:
            List of strings containing the special instructions
        """
        ingredients: List[str] = []
        if not self.__red_sauce:
            ingredients.append("Hold Red Sauce")
        if not self.__crispy_chicken:
            ingredients.append("Hold Crispy Chicken")
        return ingredients.copy()

    def __str__(self) -> str:
        """String overide method.

        Creates a string of the entree
        menu item.

        Returns:
            str representing the entree on a base
        """
        return "Chess Chicken Parm on {}".format(self.__base)

    def __eq__(self, value: object) -> bool:
        """Equals overide method.

        Checks to see if two menu items are equal.

        Args:
            value: Object representing an entree item

        Returns:
            True if items are equal;
            False if not
        """
        if isinstance(value, ChessChickenParm):
            return (self.__base == value.base and
                    self.__toppings == value.toppings and
                    self.__red_sauce == value.red_sauce and
                    self.__crispy_chicken == value.crispy_chicken)
        else:
            return False
