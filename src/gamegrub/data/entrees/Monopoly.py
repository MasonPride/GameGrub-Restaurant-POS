"""MonopolyBowl class.

This is a class that creates the Monopoly Bowl
menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
from typing import List
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings
from src.gamegrub.data.entrees.Entree import Entree


class MonopolyBowl(Entree):
    """Represents the Monopoly Bowl entree.

    This class builds the MonopolyBowl entree
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
        self.add_topping(Toppings.ONIONS)
        self.add_topping(Toppings.CHEESE)
        self.add_topping(Toppings.HOT_SAUCE)
        self.add_topping(Toppings.SOUR_CREAM)
        self.add_topping(Toppings.GUACAMOLE)
        self.add_topping(Toppings.CRISPY_STRIPS)
        self.__price: float = 17.65
        self.__spicy_beef: bool = True
        self.__veggies: bool = True
        self.__crispy_chicken: bool = True
        self.__beans: bool = True

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
        return 1685

    @property
    def spicy_beef(self) -> bool:
        """Spicy Beef attribute getter method.

        Gets the spicy beef attribute of the class.

        Returns:
            True if the entree has spicy beef;
            False if not
        """
        return self.__spicy_beef

    @spicy_beef.setter
    def spicy_beef(self, value: bool) -> None:
        """Spicy Beef attribute setter method.

        Sets the spci beef attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing ingredient
            setting
        """
        self.__spicy_beef = value

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

        Sets the veggies attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing ingredient
            setting
        """
        self.__veggies = value

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
    def beans(self) -> bool:
        """Beans attribute getter method.

        Gets the beans attribute of the class.

        Returns:
            True if the entree has beans;
            False if not
        """
        return self.__beans

    @beans.setter
    def beans(self, value: bool) -> None:
        """Beans attribute setter method.

        Sets the beans attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing ingredient
            setting
        """
        self.__beans = value

    @property
    def instructions(self) -> List[str]:
        """Shows the list of instructions.

        This method will return a list of the
        special instructions given to the entree.

        Returns:
            List of strings containing the special instructions
        """
        ingredients: List[str] = []
        if not self.__spicy_beef:
            ingredients.append("Hold Spicy Beef")
        if not self.__crispy_chicken:
            ingredients.append("Hold Crispy Chicken")
        if not self.__veggies:
            ingredients.append("Hold Veggies")
        if not self.__beans:
            ingredients.append("Hold Beans")
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
        return "Monopoly Bowl on {}".format(self.base)

    def __eq__(self, value: object) -> bool:
        """Equals overide method.

        Checks to see if two menu items are equal.

        Args:
            value: Object representing an entree item

        Returns:
            True if items are equal;
            False if not
        """
        if isinstance(value, MonopolyBowl):
            return (self.base == value.base and
                    self.toppings == value.toppings and
                    self.__spicy_beef == value.spicy_beef and
                    self.__crispy_chicken == value.crispy_chicken and
                    self.__veggies == value.veggies and
                    self.__beans == value.beans)
        else:
            return False

    @property
    def name(self) -> str:
        """Getter for name."""
        return "Monopoly Bowl"
