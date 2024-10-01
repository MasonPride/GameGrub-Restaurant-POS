"""Drink Base class.

This class creates the abstract class for all
drinks

Author: Mason Pride
Version: 0.1
"""

from src.gamegrub.data.Item import Item
from src.gamegrub.data.enums.Size import Size


class Drink(Item):
    """Drink class.

    This class creates the abstract methods to
    be used by Drink items.
    """
    def __init__(self) -> None:
        """Initialize class.

        initializes the commmon attributes for
        entrees.
        """
        self._size: Size = Size.JUNIOR

    @property
    def size(self) -> Size:
        """Size getter.

        Gets the size attribute of entree.

        Returns:
            Size attrbute of entree
        """
        return self._size

    @size.setter
    def size(self, value: Size) -> None:
        """Base setter.

        Sets the base attribute of entree.
        """
        self._size = value
