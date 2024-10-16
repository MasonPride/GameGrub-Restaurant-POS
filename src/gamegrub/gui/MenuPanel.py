"""Main Panel Class.

Creates the main panel in our GUI.

Author: Mason Pride
Version: 0.1
"""
import tkinter as tk
from src.gamegrub.data.menu.Menu import Menu
from src.gamegrub.data.sides.Side import Side
from src.gamegrub.data.entrees.Entree import Entree
from src.gamegrub.gui.sides.SidePanel import SidePanel
from src.gamegrub.gui.entrees.ChessPanel import ChessPanel
from src.gamegrub.gui.entrees.CluePanel import CluePanel
from src.gamegrub.gui.entrees.JengaPanel import JengaPanel
from src.gamegrub.gui.entrees.MonopolyPanel import MonopolyPanel
from src.gamegrub.gui.entrees.YahtzeePanel import YahtzeePanel
from src.gamegrub.data.drinks.Drink import Drink
from src.gamegrub.gui.drinks.CandyPanel import CandyPanel
from src.gamegrub.gui.drinks.CraniumPanel import CraniumPanel
from src.gamegrub.gui.drinks.SorryPanel import SorryPanel


class MenuPanel(tk.Frame):
    """Main Panel class."""

    def __init__(self, master) -> None:
        """Main panel class constructor."""
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(3, weight=1)

        i = 0
        for entree in Menu.entrees():
            self.grid_rowconfigure(i, weight=1)
            button = tk.Button(master=self, text=entree.name,
                               command=lambda x=entree.name,
                               y=entree: self.load_entree_panel(x, y))
            button.grid(row=i, column=0, padx=2, pady=2, sticky="NSEW")
            i += 1

        i = 0
        for side in Menu.sides():
            self.grid_rowconfigure(i, weight=1)
            button = tk.Button(master=self, text=str(
                               side.size + " " + side.name),
                               command=lambda x=side.name,
                               y=side: self.load_side_panel(x, y))
            button.grid(row=i, column=1, padx=2, pady=2, sticky="NSEW")
            i += 1

        i = 0
        for drink in Menu.drinks():
            self.grid_rowconfigure(i, weight=1)
            button = tk.Button(master=self, text=str(
                               drink.size + " " + drink.name),
                               command=lambda x=drink.name,
                               y=drink: self.load_drink_panel(x, y))
            button.grid(row=i, column=2, padx=2, pady=2, sticky="NSEW")
            i += 1

    def load_entree_panel(self, text: str, entree: Entree) -> None:
        """Loads the entree in their own panel.

        Args:
            text: name of the entree.
            entree: entree item.
        """
        print(text)
        if text == "Chess Chicken Parm":
            self.__master.load_panel(ChessPanel(self.__master, entree))
        if text == "Clue Chili":
            self.__master.load_panel(CluePanel(self.__master, entree))
        if text == "Jenga Nachos":
            self.__master.load_panel(JengaPanel(self.__master, entree))
        if text == "Monopoly Bowl":
            self.__master.load_panel(MonopolyPanel(self.__master, entree))
        if text == "Yahtzee Poke":
            self.__master.load_panel(YahtzeePanel(self.__master, entree))

    def load_side_panel(self, text: str, side: Side) -> None:
        """Loads the sides in their own panel.

        Args:
            text: name of the side.
            side: side item.
        """
        print(text)
        if text == "Potato Dice":
            self.__master.load_panel(SidePanel(self.__master, side))
        if text == "Risk Bites":
            self.__master.load_panel(SidePanel(self.__master, side))
        if text == "Catan Skewers":
            self.__master.load_panel(SidePanel(self.__master, side))

    def load_drink_panel(self, text: str, drink: Drink) -> None:
        """Loads the drink in their own panel.

        Args:
            text: name of the drink.
            drink: drink item.
        """
        print(text)
        if text == "Candy Land Shake":
            self.__master.load_panel(CandyPanel(self.__master, drink))
        if text == "Cranium Coffee":
            self.__master.load_panel(CraniumPanel(self.__master, drink))
        if text == "Sorry Soda":
            self.__master.load_panel(SorryPanel(self.__master, drink))
