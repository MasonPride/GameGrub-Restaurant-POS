"""YahtzeePoke class.

This is a class that creates the Yahtzee Poke
menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
from typing import List
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings
from src.gamegrub.data.entrees.Entree import Entree


class YahtzeePoke(Entree):
    """Represents the Yahtzee Poke entree.

    This class builds the YahtzeePoke entree
    menu item.
    """

    def __init__(self) -> None:
        """Initializes the class.

        Creates the MonopolyBowl object with
        preset price, calories, base, toppings,
        and ingredients.
        """
        super().__init__()
        self.base = Base.RICE
        self.add_topping(Toppings.GUACAMOLE)
        self.add_topping(Toppings.SOY_SAUCE)
        self.add_topping(Toppings.HOT_SAUCE)
        self.add_topping(Toppings.CRISPY_STRIPS)
        self.__price: float = 14.25
        self.__tuna: bool = True
        self.__veggies: bool = True
        self.__seaweed: bool = True

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
        return 785

    @property
    def tuna(self) -> bool:
        """Tuna attribute getter method.

        Gets the tuna attribute of the class.

        Returns:
            True if the entree has tuna;
            False if not
        """
        return self.__tuna

    @tuna.setter
    def tuna(self, value: bool) -> None:
        """Tuna attribute setter method.

        Sets the tuna attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing ingredient
            setting
        """
        self.__tuna = value

    @property
    def veggies(self) -> bool:
        """Veggies attribute getter method.

        Gets the veggies attribute of the class.

        Returns:
            True if the entree has veggies;
            False if not
        """
        return self.__veggies

    @veggies.setter
    def veggies(self, value: bool) -> None:
        """Veggies attribute setter method.

        Sets the veggies beef attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing ingredient
            setting
        """
        self.__veggies = value

    @property
    def seaweed(self) -> bool:
        """Seaweed attribute getter method.

        Gets the seaweed attribute of the class.

        Returns:
            True if the entree has seaweed;
            False if not
        """
        return self.__seaweed

    @seaweed.setter
    def seaweed(self, value: bool) -> None:
        """Seaweed attribute setter method.

        Sets the seaweed attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing ingredient
            setting
        """
        self.__seaweed = value

    @property
    def instructions(self) -> List[str]:
        """Shows the list of instructions.

        This method will return a list of the
        special instructions given to the entree.

        Returns:
            List of strings containing the special instructions
        """
        ingredients: List[str] = []
        if not self.__tuna:
            ingredients.append("Hold Tuna")
        if not self.__veggies:
            ingredients.append("Hold Veggies")
        if not self.__seaweed:
            ingredients.append("Hold Seaweed")
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
        return "Yahtzee Poke on {}".format(self.base)

    def __eq__(self, value: object) -> bool:
        """Equals overide method.

        Checks to see if two menu items are equal.

        Args:
            value: Object representing an entree item

        Returns:
            True if items are equal;
            False if not
        """
        if isinstance(value, YahtzeePoke):
            return (self.base == value.base and
                    self.toppings == value.toppings and
                    self.__tuna == value.tuna and
                    self.__veggies == value.veggies and
                    self.__seaweed == value.seaweed)
        else:
            return False

    @property
    def name(self) -> str:
        """Getter for name."""
        return "Yahtzee Poke"
