"""Main Panel Class.

Creates the main panel in our GUI.

Author: Mason Pride
Version: 0.1
"""
import tkinter as tk
from src.gamegrub.data.Item import Item
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
from src.gamegrub.gui.ComboPanel import ComboPanel
from src.gamegrub.data.combo.Combo import Combo
from src.gamegrub.gui.PanelFactory import PanelFactory


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
                               y=entree: self.load_item_panel(x, y))
            button.grid(row=i, column=0, padx=2, pady=2, sticky="NSEW")
            i += 1

        i = 0
        for side in Menu.sides():
            self.grid_rowconfigure(i, weight=1)
            button = tk.Button(master=self, text=str(
                               side.size + " " + side.name),
                               command=lambda x=side.name,
                               y=side: self.load_item_panel(x, y))
            button.grid(row=i, column=1, padx=2, pady=2, sticky="NSEW")
            i += 1

        i = 0
        for drink in Menu.drinks():
            self.grid_rowconfigure(i, weight=1)
            button = tk.Button(master=self, text=str(
                               drink.size + " " + drink.name),
                               command=lambda x=drink.name,
                               y=drink: self.load_item_panel(x, y))
            button.grid(row=i, column=2, padx=2, pady=2, sticky="NSEW")
            i += 1

        i = 0
        for combo in Menu.combos():
            self.grid_rowconfigure(i, weight=1)
            button = tk.Button(master=self, text=str(combo.name),
                               command=lambda x=combo.name,
                               y=combo: self.load_combo_panel(x, y))
            button.grid(row=i, column=3, padx=2, pady=2, sticky="NSEW")
            i += 1

        self.grid_rowconfigure(0, weight=1)
        c = Combo()
        combo_button = tk.Button(master=self, text=str("Custom Combo"),
                                 command=lambda x="Custom Combo":
                                 self.load_combo_panel(x, c))
        combo_button.grid(row=i, column=3, padx=2, pady=2, sticky="NSEW")


    def load_item_panel(self, text: str, item: Item) -> None:
        """Loads the item in their own panel.

        Args:
            text: name of the item.
            item: item to load.
        """
        print(text)
        panel = PanelFactory.get_panel_by_item(self.__master, item)
        self.__master.load_panel(panel)

    def load_combo_panel(self, text: str, combo: Combo = None):
        """Load Combo Panel method.

        Loads combo panel on button press

        Args:
            text: str of combo button.
        """
        print(text)
        if text == "Custom Combo":
            self.__master.load_panel(ComboPanel(self.__master))
        else:
            self.__master.load_panel(ComboPanel(self.__master, combo))
