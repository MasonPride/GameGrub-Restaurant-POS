"""Enumeration of Bases.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
from enum import Enum


class Base(Enum):
    """Enumeration of base values."""
    RICE = ("Rice", 1.0)
    SPAGHETTI = ("Spaghetti", 1.5)
    CHIPS = ("Chips", 2.0)

    def __init__(self, description: str, amount: float) -> None:
        """Constructor.

        Args:
            description: the description of the base item
            amount: the amount it costs
        """
        self.description: str = description
        self.amount: float = amount

    def __str__(self) -> str:
        """String description sizes.

        Returns:
            string description
        """
        return str(self.description)

    def __repr__(self) -> str:
        """Represenation of the Bases.

        Returns:
            string of represenation
        """
        return str(self)
