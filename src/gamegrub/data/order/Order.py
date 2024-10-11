"""Order class.

This class implements the iterator pattern.

Author: Mason Pride
Version: 0.1
"""

from src.gamegrub.data.Item import Item
from typing import Iterator, Iterable, List
from src.gamegrub.data.order.OrderNumberSingleton import OrderNumberSingleton


class Order(Iterable[Item]):
    """Iterator class for items."""

    _tax_rate: float = .115

    def __init__(self) -> None:
        """Constructor class."""
        self.__ordered_items: List[Item] = list()
        self.__order_number: int = OrderNumberSingleton(
         ).get_next_order_number()

    def add_item(self, item: Item) -> None:
        """Adds an item to the order.

        Args:
            item: the item to add
        """
        self.__ordered_items.append(item)

    def remove_item(self, item: Item) -> None:
        """Removes an item from the order.

        Args:
            item: the item to remove
        """
        self.__ordered_items.remove(item)

    def __iter__(self) -> Iterator[Item]:
        """Iterator method override.

        Retuns:
            Iterater of our list
        """
        return iter(self.__ordered_items)

    def __len__(self) -> int:
        """Length override method.

        Returns:
            int representing number of items in
            the list.
        """
        return len(self.__ordered_items)

    def __getitem__(self, position: int) -> Item:
        """Get item override method.

        Args:
            position: int representing the position.
        """
        return self.__ordered_items[position]

    @property
    def order_number(self) -> int:
        """Getter for order number.

        Retuns:
            int representing order number
        """
        return self.__order_number

    @classmethod
    def get_tax_rate(cls) -> float:
        """Class level getter.

        Gets the tax rate set at the class
        level

        Returns:
            float representing the tax rate
        """
        return cls._tax_rate

    @classmethod
    def set_tax_rate(cls, value: float) -> None:
        """Setter for tax rate.

        Args:
            value: new tax rate being set
        """
        if value >= 0.0 and value <= 1.0:
            cls._tax_rate = value
        else:
            raise TypeError("Not a valid float")

    @property
    def subtotal(self) -> float:
        """Finds the subtotal of the items.

        Adds together all the prices of
        the items in the order list

        Returns:
            float representing subtotal price
        """
        result: float = 0.0
        for item in self.__ordered_items:
            result += item.price
        return result

    @property
    def tax(self) -> float:
        """Gets the tax.

        Calculates the tax of the order.

        Returns:
            float representing tax
        """
        return self.subtotal * self.__class__().get_tax_rate()

    @property
    def total(self) -> float:
        """Calculates the total price.

        Gets the total price of the order.

        Returns:
            float representing the total price
        """
        return self.tax + self.subtotal

    @property
    def calories(self) -> int:
        """Gets the total calories of the order.

        Calculates and returns the total calories.

        Retuns:
            int representing calories
        """
        total_calories = 0
        for item in self.__ordered_items:
            total_calories += item.calories
        return total_calories
