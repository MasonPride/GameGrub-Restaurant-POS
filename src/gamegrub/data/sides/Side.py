"""Side Base class.

This class creates the abstract class for all
drinks

Author: Mason Pride
Version: 0.1
"""

from typing import List
from src.gamegrub.data.Item import Item
from src.gamegrub.data.enums.Size import Size


class Side(Item):
    """Side class.

    This class creates the abstract methods to
    be used by Side items.
    """
    def __init__(self) -> None:
        """Initialize class.

        Initializes the commmon attributes for
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
        """Size attibute setter method.

        Sets the size
        attribute of the class to the desired Size.

        Args:
            value: The desired Size from Size enum class
        """
        self._size = value

    @property
    def instructions(self) -> List[str]:
        """Instructions setter.

        Returns:
            List of instructions
        """
        instructions: List[str] = list()
        return instructions
