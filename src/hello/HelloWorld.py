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

        entree: MonopolyBowl = MonopolyBowl()
        print("    Standard entree:")
        print(entree)
        print(entree.price)

        print("\n   Change Base: ")
        entree.base = Base.SPAGHETTI
        print(entree.price)

        print("\n   Entree Toppings: ")
        print(entree.toppings)

        print("\n   Add Topping: ")
        entree.add_topping(Toppings.SOY_SAUCE)
        print(entree.toppings)

        print("\n   Remove Topping: ")
        entree.remove_topping(Toppings.ONIONS)
        print(entree.toppings)

        print("\n   Calories: ")
        print(entree.calories)

        
        print("\n   Spicy Beef Status: ")
        print(entree.spicy_beef)

        """
        print("\n   Chili Status: ")
        print(entree.chili)
        
        print("\n   Red Sauce Status: ")
        print(entree.red_sauce)
        """
        print("\n   Beans Status: ")
        print(entree.beans)
        """
        print("\n   Tuna Status: ")
        print(entree.tuna)
        """
        print("\n   Veggies: ")
        print(entree.veggies)
        """
        print("\n   Seaweed Status: ")
        print(entree.seaweed)
        """

        print("\n   Cripsy Chicken Status: ")
        print(entree.crispy_chicken)

        print("\n   Special instructions: ")
        print(entree.instructions)

        print("\n   Remove all ingredients lol: ")
        entree.spicy_beef = False
        entree.beans
        entree.crispy_chicken =False
        entree.veggies = False
        print(entree.instructions)

