"""CatanSkewers class.

This is a class that creates the Catan Skewers
side menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
from src.gamegrub.data.enums.Size import Size
from src.gamegrub.data.sides.Side import Side


class CatanSkewers(Side):
    """Represents the Catan Skewers side.

    This class builds the CatanSkewers side
    menu item.
    """

    def __init__(self) -> None:
        """Initializes the class.

        Creates the CatanSkewers object with
        preset price, calories, and size.
        """
        super().__init__()
        self.__price: float = 4.45
        self.__calories: int = 530

    @property
    def price(self) -> float:
        """Price attibute getter method.

        Gets the price attribute of the class.

        Returns:
            price attribute of the object; of type float
        """
        if self.size == Size.CLASSIC:
            self.__price = 6.85
        elif self.size == Size.WINNER:
            self.__price = 8.65
        else:
            self.__price = 4.45
        return self.__price

    @property
    def calories(self) -> int:
        """Calories attribute getter method.

        Gets the calories attribute of the class.

        Returns:
            calories attribute of the object; of type int
        """
        if self.size == Size.CLASSIC:
            self.__calories = 815
        elif self.size == Size.WINNER:
            self.__calories = 1045
        else:
            self.__calories = 530
        return self.__calories

    def __str__(self) -> str:
        """String overide method.

        Creates a string of the side
        menu item.

        Returns:
            str representing the size and side item
        """
        return "{} Catan Skewers".format(self.size)

    def __eq__(self, value: object) -> bool:
        """Equals overide method.

        Checks to see if two menu items are equal.

        Args:
            value: Object representing a side item

        Returns:
            True if items are equal;
            False if not
        """
        if isinstance(value, CatanSkewers):
            return (self.size == value.size and
                    self.__price == value.price and
                    self.__calories == value.calories)
        else:
            return False

    @property
    def name(self) -> str:
        """Getter for name."""
        return "Catan Skewers"
