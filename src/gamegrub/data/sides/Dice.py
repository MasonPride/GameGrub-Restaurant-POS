"""PotatoDice class

This is a class that creates the Potato Dice
side menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
from typing import List, Set
from src.gamegrub.data.enums.Size import Size


class PotatoDice:
    """Represents the Potato Dice side 

    This class builds the PotatoDice side 
    menu item.
    """

    def __init__(self) -> None:
        """Initializes the class

        Creates the PotatoDice object with
        preset price, calories, and size.
        """
        self.__size: Size = Size.JUNIOR
        self.__price: float = 2.75
        self.__calories: int = 350

    @property
    def size(self) -> Size:
        """Size attibute getter method

        Gets the size attribute of the class.

        Returns:
            size attribute of the class; of type Size
        """
        return self.__size

    @size.setter
    def size(self, value: Size) -> None:
        """Size attibute setter method

        Sets the size, price, and calories 
        attribute of the class to the desired Size.

        Args: 
            value: The desired Size from Size enum class
        """
        self.__size = value
        if value == Size.CLASSIC:
            self.__price = 3.85
            self.__calories = 475
        elif value == Size.WINNER:
            self.__price = 5.35
            self.__calories = 795
        else:
            self.__price = 2.75
            self.__calories = 350

    @property
    def price(self) -> float:
        """Price attibute getter method

        Gets the price attribute of the class.

        Returns:
            price attribute of the object; of type float
        """
        return self.__price

    @property
    def calories(self) -> int:
        """Calories attribute getter method

        Gets the calories attribute of the class.

        Returns:
            calories attribute of the object; of type int
        """
        return self.__calories

    def __str__(self) -> str:
        """String overide method

        Creates a string of the side
        menu item.

        Returns:
            str representing the size and side item
        """
        return "{} Potato Dice".format(self.__size)

    def __eq__(self, value: object) -> bool:
        """Equals overide method

        Checks to see if two menu items are equal.

        Args:
            value: Object representing a side item

        Returns:
            True if items are equal; 
            False if not
        """
        if isinstance(value, PotatoDice):
            return (self.__size == value.size and
                    self.__price == value.price and
                    self.__calories == value.calories)
        else:
            return False
