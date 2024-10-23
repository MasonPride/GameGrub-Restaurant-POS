"""Candy Panel class.

Handles the CandyLandShake panel in our gui.

Author: Mason Pride
Version: 0.1
"""
import tkinter as tk
from tkinter import ttk
from src.gamegrub.data.enums.Size import Size
from src.gamegrub.data.drinks.Candy import CandyLandShake


class CandyPanel(tk.Frame):
    """Candy panel class."""
    def __init__(self, master, item: CandyLandShake = None) -> None:
        """Candy panel constructor."""
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        if item is None:
            self._item = CandyLandShake()
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

        self._chocolate = tk.BooleanVar(value=bool(self._item.chocolate))
        chocolate = tk.Checkbutton(master=self, text="Chocolate",
                                   variable=self._chocolate,
                                   onvalue=True, offvalue=False)
        chocolate.grid(row=2, column=1, padx=2, pady=2, sticky="W")

        self._vanilla = tk.BooleanVar(value=bool(self._item.vanilla))
        vanilla = tk.Checkbutton(master=self, text="Vanilla",
                                 variable=self._vanilla,
                                 onvalue=True, offvalue=False)
        vanilla.grid(row=3, column=1, padx=2, pady=2, sticky="W")

        self._strawberry = tk.BooleanVar(value=bool(self._item.strawberry))
        strawberry = tk.Checkbutton(master=self, text="Strawberry",
                                    variable=self._strawberry,
                                    onvalue=True, offvalue=False)
        strawberry.grid(row=4, column=1, padx=2, pady=2, sticky="W")

        self.grid_rowconfigure(5, weight=0)
        save = tk.Button(master=self, text="Save",
                         command=lambda: self.action_performed("save"))
        save.grid(row=5, column=1, sticky="NEW")

        self.grid_rowconfigure(6, weight=1)
        cancel = tk.Button(master=self, text="Cancel",
                           command=lambda:
                           self.action_performed("cancel"))
        cancel.grid(row=6, column=1, sticky="NEW")

    def action_performed(self, text: str) -> None:
        """Action performed on button."""
        print(text)
        if text == "save":
            self._item.size = Size(self._size.get())
            self._item.vanilla = self._vanilla.get()
            self._item.chocolate = self._chocolate.get()
            self._item.strawberry = self._strawberry.get()
            self.__master.save_item(self._item)
            self.__master.load_menu_panel()
        elif text == "cancel":
            self.__master.load_menu_panel()
