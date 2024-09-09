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
    """Represents the Jenga Nachos entree

    This class builds the JengaNachos entree 
    menu item.
    """

    def __init__(self) -> None:
        """Initializes the class

        Creates the JengaNachos object with
        preset price, calories, base, toppings, 
        and ingredients.
        """
        self.__base: Base = Base.CHIPS
        self.__toppings: Set[Toppings] = {Toppings.ONIONS, 
                                            Toppings.CHEESE, 
                                            Toppings.SOUR_CREAM, 
                                            Toppings.HOT_SAUCE, 
                                            Toppings.GUACAMOLE}
        self.__price: float = 9.85
        self.__spicy_beef: bool = True
        self.__beans: bool = True

    @property
    def base(self) -> Base:
        """Base attribute getter method

        Gets the base attribute of the class.

        Returns:
            base attribute of the class; of type Base
        """
        return self.__base

    @base.setter
    def base(self, value: Base) -> None:
        """Base attribute setter method

        Sets the base, price, and calories 
        attribute of the class to the desired Size.

        Args: 
            value: The desired base from Base enum class
        """
        self.__base = value

    @property
    def toppings(self) -> Set[Toppings]:
        """Toppings attribute getter method

        Gets the toppings attribute of the class.

        Returns:
            Shallow copy of toppings attribute 
            of the object; a set containing the toppings
        """
        return self.__toppings.copy()

    def add_topping(self, value: Toppings) -> None:
        """Add toppings to object

        Adds a topping from the Toppings enum class
        to the set of toppings of the object.

        Args:
            value: The desired topping from Toppings enum
        """
        self.__toppings.add(value)

    def remove_topping(self, value: Toppings) -> None:
        """Remove toppings from object

        Removes a topping from the toppings set 

        Args:
            value: The desired topping from Toppings enum
        """
        if value in self.__toppings:
            self.__toppings.remove(value)

    @property
    def price(self) -> float:
        """Price attribute getter method

        Gets the total price attribute of the class 
        by adding the default price and base price

        Returns:
            price attribute of the object; of type float
        """
        return self.__price + self.__base.amount

    @property
    def calories(self) -> int:
        """Calories attribute getter method

        Gets the calories attribute of the class.

        Returns:
            calories attribute of the object; of type int
        """
        return 1470

    @property
    def spicy_beef(self) -> bool:
        """Spicy Beef attribute getter method

        Gets the spicy beef attribute of the class.

        Returns:
            True if the entree has spicy beef; 
            False if not
        """
        return self.__spicy_beef

    @spicy_beef.setter
    def spicy_beef(self, value: bool) -> None:
        """Spicy Beef attribute setter method

        Sets the spicy beef attribute of the class to 
        the desired setting.

        Args: 
            value: Boolean describing ingredient
            setting
        """
        self.__spicy_beef = value

    @property
    def beans(self) -> bool:
        """Beans attribute getter method

        Gets the beans attribute of the class.

        Returns:
            True if the entree has beans; 
            False if not
        """
        return self.__beans

    @beans.setter
    def beans(self, value: bool) -> None:
        """Beans attribute setter method

        Sets the beans attribute of the class to 
        the desired setting.

        Args: 
            value: Boolean describing ingredient
            setting
        """
        self.__beans = value

    @property
    def instructions(self) -> List[str]:
        """Shows the list of instructions

        This method will return a list of the 
        special instructions given to the entree.

        Returns:
            List of strings containing the special instructions
        """
        ingredients: List[str] = []
        if not self.__spicy_beef:
            ingredients.append("Hold Spicy Beef")
        if not self.__beans:
            ingredients.append("Hold Beans")
        return ingredients.copy()

    def __str__(self) -> str:
        """String overide method

        Creates a string of the entree
        menu item.

        Returns:
            str representing the entree on a base
        """
        return "Jenga Nachos on {}".format(self.__base)

    def __eq__(self, value: object) -> bool:
        """Equals overide method

        Checks to see if two menu items are equal.

        Args:
            value: Object representing an entree item

        Returns:
            True if items are equal; 
            False if not
        """
        if isinstance(value, JengaNachos):
            return (self.__base == value.base and 
                    self.__toppings == value.toppings and
                    self.__spicy_beef == value.spicy_beef and 
                    self.__beans == value.beans)
        else:
            return False
