"""Side Base class.

This class creates the abstract class for all
drinks

Author: Mason Pride
Version: 0.1
"""

from typing import List, Set
from src.gamegrub.data.Item import Item
from src.gamegrub.data.enums.Size import Size


class Side(Item):
    """Side class.

    This class creates the abstract methods to
    be used by Side items.
    """
    def __init__(self) -> None:
        """initialize class.

        initializes the commmon attributes for 
        entrees.
        """
        self.__size: Size = Size.JUNIOR

    @property
    def size(self) -> Size:
        """size getter.

        Gets the size attribute of entree.

        Returns:
            Size attrbute of entree
        """
        return self.__size

    @size.setter
    def size(self, value: Size) -> None:
        """Base setter.

        Sets the base attribute of entree.
        """
        self.__size = value
