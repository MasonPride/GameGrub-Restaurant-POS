"""Entree Base class.

This class creates the abstract class for all
entrees

Author: Mason Pride
Version: 0.1
"""

from typing import List
from src.gamegrub.data.Item import Item
from src.gamegrub.data.enums.Base import Base


class Entree(Item):
    """Entree class.

    This class creates the abstract methods to
    be used by entree items.
    """

    @property
    @abstractmethod
    def base(self) -> Base:
        raise NotImplementedError

    @base.setter
    @abstractmethod
    def base(self, value: Base) -> None:
        raise NotImplementedError