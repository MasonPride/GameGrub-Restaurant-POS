"""Order Number Singleton class.

Creates the order number singlton instance

Author: Mason Pride
Version: 0.1
"""
from typing import Optional


class OrderNumberSingleton:
    """OrderNumberSingleton class."""
    _instance: Optional["OrderNumberSingleton"] = None

    def __new__(cls) -> "OrderNumberSingleton":
        """New overide."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Constructs the singleton."""
        self._next_order_number = 1

    @staticmethod
    def get_next_order_number() -> int:
        """Gets next order number.

        Gets the next order number in the singleton.

        Returns:
            int representing the next order number
        """
        inst = OrderNumberSingleton()
        next_order_number = inst._next_order_number
        inst._next_order_number += 1
        return next_order_number
