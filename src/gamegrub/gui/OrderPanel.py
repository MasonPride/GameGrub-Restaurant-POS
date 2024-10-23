"""Order Panel Class.

Creates the side bar panel in our GUI.

Author: Mason Pride
Version: 0.1
"""
import tkinter as tk
from tkinter.ttk import Treeview, Scrollbar
from typing import Dict
from src.gamegrub.data.Item import Item
from src.gamegrub.data.sides.Side import Side
from src.gamegrub.gui.sides.SidePanel import SidePanel
from src.gamegrub.data.drinks.Candy import CandyLandShake
from src.gamegrub.gui.drinks.CandyPanel import CandyPanel
from src.gamegrub.data.drinks.Sorry import SorrySoda
from src.gamegrub.gui.drinks.SorryPanel import SorryPanel
from src.gamegrub.data.drinks.Cranium import CraniumCoffee
from src.gamegrub.gui.drinks.CraniumPanel import CraniumPanel
from src.gamegrub.data.entrees.Chess import ChessChickenParm
from src.gamegrub.gui.entrees.ChessPanel import ChessPanel
from src.gamegrub.data.entrees.Clue import ClueChili
from src.gamegrub.gui.entrees.CluePanel import CluePanel
from src.gamegrub.data.entrees.Jenga import JengaNachos
from src.gamegrub.gui.entrees.JengaPanel import JengaPanel
from src.gamegrub.data.entrees.Yahtzee import YahtzeePoke
from src.gamegrub.gui.entrees.YahtzeePanel import YahtzeePanel
from src.gamegrub.data.entrees.Monopoly import MonopolyBowl
from src.gamegrub.gui.entrees.MonopolyPanel import MonopolyPanel


class OrderPanel(tk.Frame):
    """Order Panel class."""
    def __init__(self, master) -> None:
        """Order Panel constructor."""
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        order_label = tk.Label(master=self, text="Order #")
        order_label.grid(row=0, column=0, padx=2, pady=2, sticky="E")

        self.__order_num = tk.Label(master=self, text="000")
        self.__order_num.grid(row=0, column=1, padx=2, pady=2, sticky="W")

        """
        self.__order_list = tk.Listbox(master=self)
        self.__order_list.grid(row=1, column=0, columnspan=2,
                               padx=2, pady=2, sticky="NSEW")
        """
        self.__items: Dict[str, Item] = dict()
        list_frame = tk.Frame(master=self)
        list_frame.grid_columnconfigure(0, weight=1)
        list_frame.grid_rowconfigure(0, weight=1)
        self.__order_list = Treeview(master=list_frame,
                                     show="tree", selectmode="browse")
        order_list_scrollbar = Scrollbar(master=list_frame, orient="vertical",
                                         command=self.__order_list.yview)
        self.__order_list.configure(yscroll=order_list_scrollbar.set)
        self.__order_list.grid(row=0, column=0, sticky="NSEW")
        order_list_scrollbar.grid(row=0, column=1, sticky="NSE")
        list_frame.grid(row=1, column=0, columnspan=2, sticky="NSEW")

        edit_button = tk.Button(master=self, text="Edit",
                                command=lambda:
                                self.action_performed("edit"))
        edit_button.grid(row=2, column=0, sticky="NSEW")

        delete_button = tk.Button(master=self, text="Delete",
                                  command=lambda:
                                  self.action_performed("delete"))
        delete_button.grid(row=2, column=1, sticky="NSEW")

        subtotal_label = tk.Label(master=self, text="Subtotal: $0.00")
        subtotal_label.grid(row=3, column=0, padx=2, pady=2, sticky="E")
        tax_label = tk.Label(master=self, text="Tax: $0.00")
        tax_label.grid(row=4, column=0, padx=2, pady=2, sticky="E")
        total_label = tk.Label(master=self, text="Total: $0.00")
        total_label.grid(row=5, column=0, padx=2, pady=2, sticky="E")

    def action_performed(self, text: str) -> None:
        """Handle button actions."""
        print(text)
        if text == "edit":
            node = self.__order_list.focus()
            if node:
                while node not in self.__items:
                    node = self.__order_list.parent(node)
                item: Item = self.__items[node]
                if isinstance(item, Side):
                    self.__master.load_panel(SidePanel(self.__master, item))
                elif isinstance(item, CandyLandShake):
                    self.__master.load_panel(CandyPanel(self.__master, item))
                elif isinstance(item, SorrySoda):
                    self.__master.load_panel(SorryPanel(self.__master, item))
                elif isinstance(item, CraniumCoffee):
                    self.__master.load_panel(CraniumPanel(self.__master, item))
                elif isinstance(item, ChessChickenParm):
                    self.__master.load_panel(ChessPanel(self.__master, item))
                elif isinstance(item, ClueChili):
                    self.__master.load_panel(CluePanel(self.__master, item))
                elif isinstance(item, JengaNachos):
                    self.__master.load_panel(JengaPanel(self.__master, item))
                elif isinstance(item, YahtzeePoke):
                    self.__master.load_panel(YahtzeePanel(self.__master, item))
                elif isinstance(item, MonopolyBowl):
                    self.__master.load_panel(MonopolyPanel(
                                             self.__master, item))
        elif text == "delete":
            node = self.__order_list.focus()
            if node:
                while node not in self.__items:
                    node = self.__order_list.parent(node)
                del self.__items[node]
                self.__order_list.delete(node)

    def save_item(self, item: Item) -> None:
        """Save item method.

        Saves an instance of an item to our sidebar.

        Args:
            item: Instance of an item.
        """
        for item_id, value in self.__items.items():
            if item is value:
                self.__update_tree(item, item_id)
                return
        self.__items[self.__update_tree(item)] = item

    def __update_tree(self, item: Item, index: str = "end") -> str:
        """Update tree method.

        Updates the sidebar tree.

        Args:
            item: Instance of an item.
            index: index of node.

        Returns:
            str representing an index.
        """
        if index == "end":
            index = self.__order_list.insert(parent="",
                                             index="end",
                                             text=str(item))
        else:
            self.__order_list.item(index, text=str(item))
            for child in self.__order_list.get_children(index):
                self.__order_list.delete(child)
        self.__order_list.item(index, open=True)

        for line in item.instructions:
            self.__order_list.insert(parent=index, index="end", text=line)
        return index
