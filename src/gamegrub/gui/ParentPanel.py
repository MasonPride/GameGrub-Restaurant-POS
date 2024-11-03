"""Parent Panel abstract class.

Creates the abstract parent panel class

Author: Mason Pride
Version: 0.1
"""
from abc import ABC, abstractmethod
from src.gamegrub.data.Item import Item
from typing import List


class ParentPanel(ABC):
    """Parent Panel abc class."""
    @classmethod
    def __subclasshook__(cls, subclass: type) -> None:
        if cls is ParentPanel:
            callables: Lists[str] = ['save_item',
                                     'load_order_panel']
            ret: bool = True
            for call in callables:
                ret = ret and (hasattr(subclass, call)
                and callable(getattr(subclass, call)))
            return ret
        else:
            return NotImplemented

    @abstractmethod
    def load_menu_panel(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def save_item(self, item: Item) -> None:
        raise NotImplementedError
