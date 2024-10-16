"""SorrySoda class.

This is a class that creates the Sorry Soda
drink menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from typing import List
from src.gamegrub.data.enums.Size import Size
from src.gamegrub.data.drinks.Drink import Drink


class SorrySoda(Drink):
    """Represents the Sorry Soda drink.

    This class builds the SorrySoda drink
    menu item.
    """

    def __init__(self) -> None:
        """Initializes the class.

        Creates the SorrySoda object with
        preset price, calories, size, and flavor attributes.
        """
        super().__init__()
        self.__price: float = 2.55
        self.__calories: int = 370
        self.__cola: bool = True
        self.__cherry: bool = False
        self.__grape: bool = False
        self.__orange: bool = False

    @property
    def price(self) -> float:
        """Price attribute getter method.

        Gets the price attribute of the class.

        Returns:
            price attribute of the object; of type float
        """
        if self.size == Size.CLASSIC:
            self.__price = 3.85
        elif self.size == Size.WINNER:
            self.__price = 5.35
        else:
            self.__price = 2.55
        return self.__price

    @property
    def calories(self) -> int:
        """Calories attribute getter method.

        Gets the calories attribute of the class.

        Returns:
            calories attribute of the object; of type int
        """
        if self.size == Size.CLASSIC:
            self.__calories = 535
        elif self.size == Size.WINNER:
            self.__calories = 765
        else:
            self.__calories = 370
        return self.__calories

    @property
    def cola(self) -> bool:
        """Cola attribute getter method.

        Gets the cola attribute of the class.

        Returns:
            True if the drink has cola;
            False if not
        """
        return self.__cola

    @cola.setter
    def cola(self, value: bool) -> None:
        """Cola attribute setter method.

        Sets the cola attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing flavor
            setting
        """
        self.__cola = value

    @property
    def cherry(self) -> bool:
        """Cherry attribute getter method.

        Gets the cherry attribute of the class.

        Returns:
            True if the drink has cherry;
            False if not
        """
        return self.__cherry

    @cherry.setter
    def cherry(self, value: bool) -> None:
        """Cherry attribute setter method.

        Sets the cherry attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing flavor
            setting
        """
        self.__cherry = value

    @property
    def grape(self) -> bool:
        """Grape attribute getter method.

        Gets the grape attribute of the class.

        Returns:
            True if the drink has grape;
            False if not
        """
        return self.__grape

    @grape.setter
    def grape(self, value: bool) -> None:
        """Grape attribute setter method.

        Sets the grape attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing flavor
            setting
        """
        self.__grape = value

    @property
    def orange(self) -> bool:
        """Orange attribute getter method.

        Gets the orange attribute of the class.

        Returns:
            True if the drink has orange;
            False if not
        """
        return self.__orange

    @orange.setter
    def orange(self, value: bool) -> None:
        """Orange attribute setter method.

        Sets the orange attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing flavor
            setting
        """
        self.__orange = value

    @property
    def instructions(self) -> List[str]:
        """Shows the list of instructions.

        This method will return a list of the
        special instructions given to the drink.

        Returns:
            List of strings containing the special instructions
        """
        instruct: List[str] = []
        if not self.__cola:
            instruct.append("Hold Cola")
        if self.__cherry:
            instruct.append("Add Cherry")
        if self.__grape:
            instruct.append("Add Grape")
        if self.__orange:
            instruct.append("Add Orange")
        return instruct.copy()

    def __str__(self) -> str:
        """String overide method.

        Creates a string of the drink
        menu item.

        Returns:
            str representing the size and drink
        """
        return "{} Sorry Soda".format(self.size)

    def __eq__(self, value: object) -> bool:
        """Equals overide method.

        Checks to see if two menu items are equal.

        Args:
            value: Object representing a drink item

        Returns:
            True if items are equal;
            False if not
        """
        if isinstance(value, SorrySoda):
            return (self.size == value.size and
                    self.__price == value.price and
                    self.__calories == value.calories and
                    self.__cola == value.cola and
                    self.__cherry == value.cherry and
                    self.__grape == value.grape and
                    self.__orange == value.orange)
        else:
            return False

    @property
    def name(self) -> str:
        """Getter for name."""
        return "Sorry Soda"
