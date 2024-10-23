"""ChessChickenParm class.

This is a class that creates the Chess Chicken Parm
menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
from typing import List
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings
from src.gamegrub.data.entrees.Entree import Entree


class ChessChickenParm(Entree):
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
        super().__init__()
        self.base = Base.SPAGHETTI
        self.add_topping(Toppings.CHEESE)
        self.add_topping(Toppings.FRESH_HERBS)
        self.__price: float = 12.15
        self.__red_sauce: bool = True
        self.__crispy_chicken: bool = True

    @property
    def price(self) -> float:
        """Price attribute getter method.

        Gets the total price attribute of the class
        by adding the default price and base price

        Returns:
            price attribute of the object; of type float
        """
        return self.__price + self.base.amount

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
        for item in super().instructions():
            ingredients.append(item)
        return ingredients

    def __str__(self) -> str:
        """String overide method.

        Creates a string of the entree
        menu item.

        Returns:
            str representing the entree on a base
        """
        return "Chess Chicken Parm on {}".format(self.base)

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
            return (self.base == value.base and
                    self.toppings == value.toppings and
                    self.__red_sauce == value.red_sauce and
                    self.__crispy_chicken == value.crispy_chicken)
        else:
            return False

    @property
    def name(self) -> str:
        """Getter for name."""
        return "Chess Chicken Parm"
