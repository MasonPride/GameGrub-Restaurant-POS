"""Cranium Panel class.

Handles the CraniumCoffee panel in our gui.

Author: Mason Pride
Version: 0.1
"""
import tkinter as tk
from tkinter import ttk
from src.gamegrub.data.enums.Size import Size


class CraniumPanel(tk.Frame):
    """Cranium panel class."""
    def __init__(self, master, item) -> None:
        """Cranium panel constructor."""
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        self.__item = item

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        title = tk.Label(master=self, text=self.__item.name)
        title.grid(row=0, column=1, padx=2, pady=2, sticky="SEW")

        self.__size = tk.StringVar(value=(self.__item.size))
        size_combo = ttk.Combobox(master=self, textvariable=self.__size)
        size_combo['values'] = [str(x) for x in Size]
        size_combo.grid(row=1, column=1, padx=2, pady=2, sticky="W")

        self.__milk = tk.BooleanVar(value=bool(self.__item.milk))
        milk = tk.Checkbutton(master=self, text="Milk",
                              variable=self.__milk,
                              onvalue=True, offvalue=False)
        milk.grid(row=2, column=1, padx=2, pady=2, sticky="W")

        self.__caramel = tk.BooleanVar(value=bool(self.__item.caramel))
        caramel = tk.Checkbutton(master=self, text="Caramel",
                                 variable=self.__caramel,
                                 onvalue=True, offvalue=False)
        caramel.grid(row=3, column=1, padx=2, pady=2, sticky="W")

        self.__chocolate = tk.BooleanVar(value=bool(self.__item.chocolate))
        chocolate = tk.Checkbutton(master=self, text="Chocolate",
                                   variable=self.__chocolate,
                                   onvalue=True, offvalue=False)
        chocolate.grid(row=4, column=1, padx=2, pady=2, sticky="W")

        self.__mint = tk.BooleanVar(value=bool(self.__item.mint))
        mint = tk.Checkbutton(master=self, text="Mint",
                              variable=self.__mint,
                              onvalue=True, offvalue=False)
        mint.grid(row=5, column=1, padx=2, pady=2, sticky="W")

        self.grid_rowconfigure(6, weight=1)
        save = tk.Button(master=self, text="Save",
                         command=lambda: self.action_performed("save"))
        save.grid(row=6, column=1, sticky="NEW")

    def action_performed(self, text):
        """Action performed on button."""
        print(text)
        if text == "save":
            self.__master.load_menu_panel()
