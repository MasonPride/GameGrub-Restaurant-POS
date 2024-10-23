"""SorryPanel class.

Handles the Sorry panel in our gui.

Author: Mason Pride
Version: 0.1
"""
import tkinter as tk
from tkinter import ttk
from src.gamegrub.data.enums.Size import Size
from src.gamegrub.data.drinks.Sorry import SorrySoda


class SorryPanel(tk.Frame):
    """Sorry panel class."""
    def __init__(self, master, item: SorrySoda = None) -> None:
        """Sorry panel constructor."""
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        if item is None:
            self._item = SorrySoda()
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

        self._cola = tk.BooleanVar(value=bool(self._item.cola))
        cola = tk.Checkbutton(master=self, text="Cola",
                              variable=self._cola,
                              onvalue=True, offvalue=False)
        cola.grid(row=2, column=1, padx=2, pady=2, sticky="W")

        self._cherry = tk.BooleanVar(value=bool(self._item.cherry))
        cherry = tk.Checkbutton(master=self, text="Cherry",
                                variable=self._cherry,
                                onvalue=True, offvalue=False)
        cherry.grid(row=3, column=1, padx=2, pady=2, sticky="W")

        self._grape = tk.BooleanVar(value=bool(self._item.grape))
        grape = tk.Checkbutton(master=self, text="Grape",
                               variable=self._grape,
                               onvalue=True, offvalue=False)
        grape.grid(row=4, column=1, padx=2, pady=2, sticky="W")

        self._orange = tk.BooleanVar(value=bool(self._item.orange))
        orange = tk.Checkbutton(master=self, text="Orange",
                                variable=self._orange,
                                onvalue=True, offvalue=False)
        orange.grid(row=5, column=1, padx=2, pady=2, sticky="W")

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
            self._item.cola = self._cola.get()
            self._item.cherry = self._cherry.get()
            self._item.grape = self._grape.get()
            self._item.orange = self._orange.get()
            self.__master.save_item(self._item)
            self.__master.load_menu_panel()
        elif text == "cancel":
            self.__master.load_menu_panel()
