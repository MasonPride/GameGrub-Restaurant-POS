"""CraniumCoffee class.

This is a class that creates the Cranium Coffee
drink menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from typing import List
from src.gamegrub.data.enums.Size import Size
from src.gamegrub.data.drinks.Drink import Drink


class CraniumCoffee(Drink):
    """Represents the Cranium Coffee drink.

    This class builds the CraniumCoffee drink
    menu item.
    """

    def __init__(self) -> None:
        """Initializes the class.

        Creates the CraniumCoffee object with
        preset price, calories, size, and flavor attributes.
        """
        super().__init__()
        self.__price: float = 4.35
        self.__calories: int = 380
        self.__milk: bool = True
        self.__caramel: bool = False
        self.__chocolate: bool = False
        self.__mint: bool = False

    @property
    def price(self) -> float:
        """Price attribute getter method.

        Gets the price attribute of the class.

        Returns:
            price attribute of the object; of type float
        """
        if self.size == Size.CLASSIC:
            self.__price = 5.25
        elif self.size == Size.WINNER:
            self.__price = 6.00
        else:
            self.__price = 4.35
        return self.__price

    @property
    def calories(self) -> int:
        """Calories attribute getter method.

        Gets the calories attribute of the class.

        Returns:
            calories attribute of the object; of type int
        """
        if self.size == Size.CLASSIC:
            self.__calories = 495
        elif self.size == Size.WINNER:
            self.__calories = 585
        else:
            self.__calories = 380
        return self.__calories

    @property
    def milk(self) -> bool:
        """Milk attribute getter method.

        Gets the milk attribute of the class.

        Returns:
            True if the drink has milk;
            False if not
        """
        return self.__milk

    @milk.setter
    def milk(self, value: bool) -> None:
        """Milk attribute setter method.

        Sets the milk attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing flavor
            setting
        """
        self.__milk = value

    @property
    def caramel(self) -> bool:
        """Caramel attribute getter method.

        Gets the caramel attribute of the class.

        Returns:
            True if the drink has caramel;
            False if not
        """
        return self.__caramel

    @caramel.setter
    def caramel(self, value: bool) -> None:
        """Caramel attribute setter method.

        Sets the caramel attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing flavor
            setting
        """
        self.__caramel = value

    @property
    def chocolate(self) -> bool:
        """Chocolate attribute getter method.

        Gets the chocolate attribute of the class.

        Returns:
            True if the drink has chocolate;
            False if not
        """
        return self.__chocolate

    @chocolate.setter
    def chocolate(self, value: bool) -> None:
        """Chocolate attribute setter method.

        Sets the chocolate attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing flavor
            setting
        """
        self.__chocolate = value

    @property
    def mint(self) -> bool:
        """Mint attribute getter method.

        Gets the mint attribute of the class.

        Returns:
            True if the drink has mint;
            False if not
        """
        return self.__mint

    @mint.setter
    def mint(self, value: bool) -> None:
        """Mint attribute setter method.

        Sets the mint attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing flavor
            setting
        """
        self.__mint = value

    @property
    def instructions(self) -> List[str]:
        """Shows the list of instructions.

        This method will return a list of the
        special instructions given to the drink.

        Returns:
            List of strings containing the special instructions
        """
        instruct: List[str] = []
        if not self.__milk:
            instruct.append("Hold Milk")
        if self.__caramel:
            instruct.append("Add Caramel")
        if self.__chocolate:
            instruct.append("Add Chocolate")
        if self.__mint:
            instruct.append("Add Mint")
        return instruct.copy()

    def __str__(self) -> str:
        """String overide method.

        Creates a string of the drink
        menu item.

        Returns:
            str representing the size and drink
        """
        return "{} Cranium Coffee".format(self.size)

    def __eq__(self, value: object) -> bool:
        """Equals overide method.

        Checks to see if two menu items are equal.

        Args:
            value: Object representing a drink item

        Returns:
            True if items are equal;
            False if not
        """
        if isinstance(value, CraniumCoffee):
            return (self.size == value.size and
                    self.__price == value.price and
                    self.__calories == value.calories and
                    self.__milk == value.milk and
                    self.__caramel == value.caramel and
                    self.__chocolate == value.chocolate and
                    self.__mint == value.mint)
        else:
            return False

    @property
    def name(self) -> str:
        """Getter for name."""
        return "Cranium Coffee"
