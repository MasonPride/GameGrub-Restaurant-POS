from enum import Enum

class Toppings(str, Enum):
    ONIONS = "Onions"
    CHEESE = "Cheese"
    HOT_SAUCE = "Hot Sauce"
    SOUR_CREAM = "Sour Cream"
    GUACAMOLE = "Guacamole"
    SOY_SAUCE = "Soy Sauce"
    CRISPY_STRIPS = "Crispy Strips"
    FRESH_HERBS = "Fresh Herbs"

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self)
