"""ClueChili class.

This is a class that creates the Clue Chili
menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
from typing import List
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings
from src.gamegrub.data.entrees.Entree import Entree


class ClueChili(Entree):
    """Represents the Clue Chili entree.

    This class builds the ClueChili entree
    menu item.
    """

    def __init__(self) -> None:
        """Initializes the class.

        Creates the ClueChili object with
        preset price, calories, base, toppings,
        and ingredients.
        """
        super().__init__()
        self.base = Base.SPAGHETTI
        self.add_topping(Toppings.ONIONS)
        self.add_topping(Toppings.CHEESE)
        self.add_topping(Toppings.HOT_SAUCE)
        self.__price: float = 8.95
        self.__spicy_beef: bool = True
        self.__chili: bool = True
        self.__red_sauce: bool = True
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
        return 1165

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

        Sets the spicy beef attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing ingredient
            setting
        """
        self.__spicy_beef = value

    @property
    def chili(self) -> bool:
        """Chili attribute getter method.

        Gets the chili attribute of the class.

        Returns:
            True if the entree has chili;
            False if not
        """
        return self.__chili

    @chili.setter
    def chili(self, value: bool) -> None:
        """Chili attribute setter method.

        Sets the chili attribute of the class to
        the desired setting.

        Args:
            value: Boolean describing ingredient
            setting
        """
        self.__chili = value

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
        # ingredients: List[str] = super().instructions()
        if not self.__spicy_beef:
            ingredients.append("Hold Spicy Beef")
        if not self.__chili:
            ingredients.append("Hold Chili")
        if not self.__red_sauce:
            ingredients.append("Hold Red Sauce")
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
        return "Clue Chili on {}".format(self.base)

    def __eq__(self, value: object) -> bool:
        """Equals overide method.

        Checks to see if two menu items are equal.

        Args:
            value: Object representing an entree item

        Returns:
            True if items are equal;
            False if not
        """
        if isinstance(value, ClueChili):
            return (self.base == value.base and
                    self.toppings == value.toppings and
                    self.__spicy_beef == value.spicy_beef and
                    self.__chili == value.chili and
                    self.__red_sauce == value.red_sauce and
                    self.__beans == value.beans)
        else:
            return False

    @property
    def name(self) -> str:
        """Getter for name."""
        return "Clue Chili"
