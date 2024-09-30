"""Order class.

This class implements the iterator pattern.

Author: Mason Pride
Version: 0.1
"""

from src.gamegrub.data.Item import Item
from typing import Iterator, Iterable, List

class Order(Iterable[Item]):
    """Iterator class for items."""

    __tax_rate: float = .115
    
    def __init__(self) -> None:
        """Constructor class."""
        self.__ordered_items: List[Item] = list()
        self.__order_number: int = 0

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
        """iterator method override."""
        return iter(self.__ordered_items)

    def __len__(self) -> int:
        """length override method."""
        return len(self.__ordered_items)

    def __getitem__(self, position: int) -> Item:
        """get item override method."""
        return self.__ordered_items[position]