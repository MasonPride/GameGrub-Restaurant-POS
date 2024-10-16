"""SorryPanel class.

Handles the Sorry panel in our gui.

Author: Mason Pride
Version: 0.1
"""
import tkinter as tk
from tkinter import ttk
from src.gamegrub.data.enums.Size import Size


class SorryPanel(tk.Frame):
    """Sorry panel class."""
    def __init__(self, master, item) -> None:
        """Sorry panel constructor."""
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

        self.__cola = tk.BooleanVar(value=bool(self.__item.cola))
        cola = tk.Checkbutton(master=self, text="Cola",
                              variable=self.__cola,
                              onvalue=True, offvalue=False)
        cola.grid(row=2, column=1, padx=2, pady=2, sticky="W")

        self.__cherry = tk.BooleanVar(value=bool(self.__item.cherry))
        cherry = tk.Checkbutton(master=self, text="Cherry",
                                variable=self.__cherry,
                                onvalue=True, offvalue=False)
        cherry.grid(row=3, column=1, padx=2, pady=2, sticky="W")

        self.__grape = tk.BooleanVar(value=bool(self.__item.grape))
        grape = tk.Checkbutton(master=self, text="Grape",
                               variable=self.__grape,
                               onvalue=True, offvalue=False)
        grape.grid(row=4, column=1, padx=2, pady=2, sticky="W")

        self.__orange = tk.BooleanVar(value=bool(self.__item.orange))
        orange = tk.Checkbutton(master=self, text="Orange",
                                variable=self.__orange,
                                onvalue=True, offvalue=False)
        orange.grid(row=5, column=1, padx=2, pady=2, sticky="W")

        self.grid_rowconfigure(6, weight=1)
        save = tk.Button(master=self, text="Save",
                         command=lambda: self.action_performed("save"))
        save.grid(row=6, column=1, sticky="NEW")

    def action_performed(self, text):
        """Action performed on button."""
        print(text)
        if text == "save":
            self.__master.load_menu_panel()
