from enum import Enum

class Base(str, Enum):
    RICE = "Rice"
    SPAGHETTI = "Spaghetti"
    CHIPS = "Chips"

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self)
