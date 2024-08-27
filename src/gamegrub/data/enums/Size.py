from enum import Enum

class Size(str, Enum):
    JUNIOR = "Junior"
    CLASSIC = "Classic"
    WINNER = "Winner"

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self)
