"""Sample HelloWorld Program.

This is a sample HelloWorld program to demonstrate proper
Python coding style, testing, documentation, and more.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
from typing import List
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Size import Size
from src.gamegrub.data.enums.Toppings import Toppings
from src.gamegrub.data.entrees.Clue import ClueChili
from src.gamegrub.data.entrees.Jenga import JengaNachos
from src.gamegrub.data.entrees.Yahtzee import YahtzeePoke
from src.gamegrub.data.entrees.Chess import ChessChickenParm
from src.gamegrub.data.entrees.Monopoly import MonopolyBowl
from src.gamegrub.data.sides.Dice import PotatoDice
from src.gamegrub.data.drinks.Candy import CandyLandShake


class HelloWorld:
    """Simple HelloWorld Class.

    Prints "Hello World" to the terminal when the main function is executed.
    """

    @staticmethod
    def main(args: List[str]) -> None:
        """Prints a hello message.

        This method prints the standard "Hello World" message to the terminal.

        Args:
            args: The command-line arguments provided to the program.
        """
        if len(args) == 2:
            print("Hello {}".format(args[1]))
        else:
            print("Hello World")

        
        drink: CandyLandShake = CandyLandShake()
        print(drink)
        print(drink.price)
        print(drink.calories)
        
        drink.chocolate = False
        drink.vanilla = True
        drink.strawberry = True
        print(drink.instructions)