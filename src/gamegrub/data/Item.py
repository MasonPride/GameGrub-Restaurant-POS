"""Item interface class.

Author: Mason Pride
Version: 0.1
"""

from abc import ABC, abstractmethod
from typing import List


class Item(ABC):
    """Item class.

    This class creates the abstract methods to
    be used by menu items.
    """
    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        """Subclass hook.

        Makes sure the item is able to inherit.
        """
        if cls is Item:
            callables: List[str] = ['price', 'calories', 'instructions']
            ret = True
            for call in callables:
                ret = ret and (hasattr(subclass, call) and
                               callable(getattr(subclass, call)))
            return ret
        else:
            return NotImplemented

    @property
    @abstractmethod
    def price(self) -> float:
        """Price getter.

        Raises NotImplementedError.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def calories(self) -> int:
        """Calories getter.

        Raises NotImplementedError.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def instructions(self) -> List[str]:
        """Instructions getter.

        Raises NotImplementedError.
        """
        raise NotImplementedError
