"""Clue Chili Panel class."""
import tkinter as tk
from tkinter import ttk
from src.gamegrub.data.entrees.Clue import ClueChili
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings


class CluePanel(tk.Frame):
    """Clue Panel class."""
    def __init__(self, master, item) -> None:
        """Clue Panel constructor."""
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        self.__item = item

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        title = tk.Label(master=self, text=self.__item.name)
        title.grid(row=0, column=1, padx=2, pady=2, sticky="SEW")

        self.__base = tk.StringVar(value=(self.__item.base))
        base_combo = ttk.Combobox(master=self, textvariable=self.__base)
        base_combo['values'] = [str(x) for x in Base]
        base_combo.grid(row=1, column=1, padx=2, pady=2, sticky="W")

        self.__red_sauce = tk.BooleanVar(value=bool(self.__item.red_sauce))
        red_sauce = tk.Checkbutton(master=self, text="Red Sauce", variable=self.__red_sauce, onvalue=True, offvalue=False)
        red_sauce.grid(row=2, column=1, padx=2, pady=2, sticky="W")

        self.__spicy_beef = tk.BooleanVar(value=bool(self.__item.spicy_beef))
        spicy_beef = tk.Checkbutton(master=self, text="Spicy Beef", variable=self.__spicy_beef, onvalue=True, offvalue=False)
        spicy_beef.grid(row=3, column=1, padx=2, pady=2, sticky="W")

        self.__chili = tk.BooleanVar(value=bool(self.__item.chili))
        chili = tk.Checkbutton(master=self, text="Chili", variable=self.__chili, onvalue=True, offvalue=False)
        chili.grid(row=4, column=1, padx=2, pady=2, sticky="W")

        self.__beans = tk.BooleanVar(value=bool(self.__item.beans))
        beans = tk.Checkbutton(master=self, text="Beans", variable=self.__beans, onvalue=True, offvalue=False)
        beans.grid(row=5, column=1, padx=2, pady=2, sticky="W")

        top_label = tk.Label(master=self, text="Toppings")
        top_label.grid(row=6, column=1, padx=2, pady=2, sticky="EW")

        i = 7
        self.__toppings = dict()
        for t in Toppings:
            self.__toppings[t] = tk.BooleanVar(value=(t in self.__item.toppings))
            check = tk.Checkbutton(master=self, text=str(t), variable=self.__toppings[t], onvalue=True, offvalue=False)
            check.grid(row=i, column=1, padx=2, pady=2, sticky="W")
            i +=1 
        
        self.grid_rowconfigure(i, weight=1)
        save = tk.Button(master=self, text="Save", command=lambda: self.action_performed("save"))
        save.grid(row = i, column = 1, sticky="NEW")

    def action_performed(self, text):
        """Performs the save button action."""
        print(text)
        if text == "save":
            self.__master.load_menu_panel()
