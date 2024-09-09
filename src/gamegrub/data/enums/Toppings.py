"""Enumeration of Toppings.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
from enum import Enum


class Toppings(str, Enum):
    """Enumeration of topping values."""
    ONIONS = "Onions"
    CHEESE = "Cheese"
    HOT_SAUCE = "Hot Sauce"
    SOUR_CREAM = "Sour Cream"
    GUACAMOLE = "Guacamole"
    SOY_SAUCE = "Soy Sauce"
    CRISPY_STRIPS = "Crispy Strips"
    FRESH_HERBS = "Fresh Herbs"

    def __str__(self) -> str:
        """String description toppings.

        Returns:
            string description
        """
        return str(self.value)

    def __repr__(self) -> str:
        """Represenation of the toppings.

        Returns:
            string of represenation
        """
        return str(self)
