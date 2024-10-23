"""Primary Window class.

Represents the main GUI window

Author: Mason Pride
Version: 0.1
"""
import tkinter as tk
from src.gamegrub.gui.MenuPanel import MenuPanel
from src.gamegrub.gui.OrderPanel import OrderPanel
from src.gamegrub.data.Item import Item


class PrimaryWindow(tk.Tk):
    """Primary Window class."""

    def __init__(self) -> None:
        """Primary Window constructor."""
        tk.Tk.__init__(self)
        self.minsize(width=700, height=400)
        self.title("Game Grub")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=2)

        self.__main = None
        self.load_menu_panel()

        self.__sidebar = OrderPanel(self)
        self.__sidebar.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")

    def load_menu_panel(self) -> None:
        """Loads the menu panel."""
        self.load_panel(MenuPanel(self))

    def load_panel(self, panel):
        """Load panel.

        Loads the given panel.

        Args:
            panel: Panel to be loaded.
        """
        if self.__main is not None:
            self.__main.destroy()
        self.__main = panel
        self.__main.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

    def save_item(self, item: Item) -> None:
        """Saves item to sidebar.

        Args:
            item: Item to save.
        """
        self.__sidebar.save_item(item)
