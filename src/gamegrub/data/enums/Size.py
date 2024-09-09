"""Enumeration of Sides.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
from enum import Enum


class Size(str, Enum):
    """Enumeration of size values."""
    JUNIOR = "Junior"
    CLASSIC = "Classic"
    WINNER = "Winner"

    def __str__(self) -> str:
        """String description sizes.

        Returns:
            string description
        """
        return str(self.value)

    def __repr__(self) -> str:
        """Represenation of the sizes.

        Returns:
            string of represenation
        """
        return str(self)
