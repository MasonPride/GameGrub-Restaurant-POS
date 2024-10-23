"""Cranium Panel class.

Handles the CraniumCoffee panel in our gui.

Author: Mason Pride
Version: 0.1
"""
import tkinter as tk
from tkinter import ttk
from src.gamegrub.data.enums.Size import Size
from src.gamegrub.data.drinks.Cranium import CraniumCoffee


class CraniumPanel(tk.Frame):
    """Cranium panel class."""
    def __init__(self, master, item: CraniumCoffee = None) -> None:
        """Cranium panel constructor."""
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        if item is None:
            self._item = CraniumCoffee()
        else:
            self._item = item

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        title = tk.Label(master=self, text=self._item.name)
        title.grid(row=0, column=1, padx=2, pady=2, sticky="SEW")

        self._size = tk.StringVar(value=(self._item.size))
        size_combo = ttk.Combobox(master=self, textvariable=self._size)
        size_combo['values'] = [str(x) for x in Size]
        size_combo.grid(row=1, column=1, padx=2, pady=2, sticky="W")

        self._milk = tk.BooleanVar(value=bool(self._item.milk))
        milk = tk.Checkbutton(master=self, text="Milk",
                              variable=self._milk,
                              onvalue=True, offvalue=False)
        milk.grid(row=2, column=1, padx=2, pady=2, sticky="W")

        self._caramel = tk.BooleanVar(value=bool(self._item.caramel))
        caramel = tk.Checkbutton(master=self, text="Caramel",
                                 variable=self._caramel,
                                 onvalue=True, offvalue=False)
        caramel.grid(row=3, column=1, padx=2, pady=2, sticky="W")

        self._chocolate = tk.BooleanVar(value=bool(self._item.chocolate))
        chocolate = tk.Checkbutton(master=self, text="Chocolate",
                                   variable=self._chocolate,
                                   onvalue=True, offvalue=False)
        chocolate.grid(row=4, column=1, padx=2, pady=2, sticky="W")

        self._mint = tk.BooleanVar(value=bool(self._item.mint))
        mint = tk.Checkbutton(master=self, text="Mint",
                              variable=self._mint,
                              onvalue=True, offvalue=False)
        mint.grid(row=5, column=1, padx=2, pady=2, sticky="W")

        self.grid_rowconfigure(6, weight=0)
        save = tk.Button(master=self, text="Save",
                         command=lambda: self.action_performed("save"))
        save.grid(row=6, column=1, sticky="NEW")

        self.grid_rowconfigure(7, weight=1)
        cancel = tk.Button(master=self, text="Cancel",
                           command=lambda:
                           self.action_performed("cancel"))
        cancel.grid(row=7, column=1, sticky="NEW")

    def action_performed(self, text: str) -> None:
        """Action performed on button."""
        print(text)
        if text == "save":
            self._item.size = Size(self._size.get())
            self._item.milk = self._milk.get()
            self._item.chocolate = self._chocolate.get()
            self._item.mint = self._mint.get()
            self._item.caramel = self._caramel.get()
            self.__master.save_item(self._item)
            self.__master.load_menu_panel()
        elif text == "cancel":
            self.__master.load_menu_panel()
