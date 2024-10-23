"""Chess Chicken Parm Panel class."""
import tkinter as tk
from tkinter import ttk
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings
from src.gamegrub.data.entrees.Chess import ChessChickenParm


class ChessPanel(tk.Frame):
    """Chess Panel class."""
    def __init__(self, master, item: ChessChickenParm = None) -> None:
        """Chess Panel constructor."""
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        if item is None:
            self._item = ChessChickenParm()
        else:
            self._item = item

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        title = tk.Label(master=self, text=self._item.name)
        title.grid(row=0, column=1, padx=2, pady=2, sticky="SEW")

        self._base = tk.StringVar(value=(self._item.base))
        base_combo = ttk.Combobox(master=self, textvariable=self._base)
        base_combo['values'] = [str(x) for x in Base]
        base_combo.grid(row=1, column=1, padx=2, pady=2, sticky="W")

        self._red_sauce = tk.BooleanVar(value=bool(self._item.red_sauce))
        red_sauce = tk.Checkbutton(master=self, text="Red Sauce",
                                   variable=self._red_sauce,
                                   onvalue=True, offvalue=False)
        red_sauce.grid(row=2, column=1, padx=2, pady=2, sticky="W")

        self._crispy_chicken = tk.BooleanVar(value=bool(
                                              self._item.crispy_chicken))
        crispy_chicken = tk.Checkbutton(master=self, text="Crispy Chicken",
                                        variable=self._crispy_chicken,
                                        onvalue=True, offvalue=False)
        crispy_chicken.grid(row=3, column=1, padx=2, pady=2, sticky="W")

        top_label = tk.Label(master=self, text="Toppings")
        top_label.grid(row=4, column=1, padx=2, pady=2, sticky="EW")

        i = 5
        self._toppings = dict()
        for t in Toppings:
            self._toppings[t] = tk.BooleanVar(value=(
                                               t in self._item.toppings))
            check = tk.Checkbutton(master=self, text=str(t),
                                   variable=self._toppings[t],
                                   onvalue=True, offvalue=False)
            check.grid(row=i, column=1, padx=2, pady=2, sticky="W")
            i += 1

        self.grid_rowconfigure(i, weight=1)
        save = tk.Button(master=self, text="Save",
                         command=lambda: self.action_performed("save"))
        save.grid(row=i, column=1, sticky="NEW")

        self.grid_rowconfigure(i, weight=1)
        cancel = tk.Button(master=self, text="Cancel",
                           command=lambda:
                           self.action_performed("cancel"))
        cancel.grid(row=i+1, column=1, sticky="NEW")

    def action_performed(self, text: str) -> None:
        """Performs the save button action."""
        print(text)
        if text == "save":
            if self._base.get() == "Spaghetti":
                self._item.base = Base.SPAGHETTI
            elif self._base.get() == "Rice":
                self._item.base = Base.RICE
            elif self._base.get() == "Chips":
                self._item.base = Base.CHIPS
            self._item.red_sauce = self._red_sauce.get()
            self._item.crispy_chicken = self._crispy_chicken.get()
            for t in Toppings:
                if self._toppings[t].get():
                    self._item.add_topping(t)
                else:
                    self._item.remove_topping(t)
            self.__master.save_item(self._item)
            self.__master.load_menu_panel()
        elif text == "cancel":
            self.__master.load_menu_panel()
