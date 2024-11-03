"""ComboPanel class.

Creates the combo panel window

Author: Mason Pride
Version: 0.1
"""
from tkinter import Frame, StringVar, Button
from tkinter.ttk import Combobox
from src.gamegrub.gui.ParentPanel import ParentPanel
from src.gamegrub.data.Item import Item
from src.gamegrub.data.entrees.Entree import Entree
from src.gamegrub.data.drinks.Drink import Drink
from src.gamegrub.data.sides.Side import Side
from src.gamegrub.gui.entrees.EntreePanel import EntreePanel
from src.gamegrub.gui.drinks.DrinkPanel import DrinkPanel
from src.gamegrub.gui.sides.SideBasePanel import SideBasePanel
from src.gamegrub.data.combo.Combo import Combo


class ComboPanel(Frame, ParentPanel):
    """Combo Panel class."""

    def __init__(self, master, combo: Combo = None) -> None:
        """Constructs the panel."""
        self.__master = master
        Frame.__init__(self, master=master)
        self.__combo = combo
        if combo is not None:
            self.__entree = combo.entree
            self.__side = combo.side
            self.__drink = combo.drink

        self._entree_var = StringVar(value=str(""))
        entree_combo = Combobox(master=self, textvariable=self._entree_var)
        entree_combo['values'] = ["None", "Chess Chicken Parm",
                                  "Clue Chili", "Jenga Nachos",
                                  "Monopoly Bowl", "Yahtzee Poke"]
        entree_combo.grid(row=0, column=0, padx=2, pady=2, sticky="NEW")

        self._side_var = StringVar(value=str(""))
        side_combo = Combobox(master=self, textvariable=self._side_var)
        side_combo['values'] = ["None", "Potato Dice", "Risk Bites",
                                "Catan Skewers"]
        side_combo.grid(row=0, column=1, padx=2, pady=2, sticky="NEW")

        self._drink_var = StringVar(value=str(""))
        drink_combo = Combobox(master=self, textvariable=self._drink_var)
        drink_combo['values'] = ["None", "Candy Land Shake", "Sorry Soda",
                                "CraniumCoffee"]
        drink_combo.grid(row=0, column=2, padx=2, pady=2, sticky="NEW")

        self._entree_panel: EntreePanel = EntreePanel(self)
        self._side_panel: SideBasePanel = SideBasePanel(self)
        self._drink_panel: DrinkPanel = DrinkPanel(self)
        if self.__combo is not None:
            pass
        else:
            self._entree_var.set("None")
            self._side_var.set("None")
            self._drink_var.set("None")
        self._entree_panel.grid(row=1, column=0, padx=2, pady=2, sticky="NSEW")
        self._side_panel.grid(row=1, column=1, padx=2, pady=2, sticky="NSEW")
        self._drink_panel.grid(row=1, column=2, padx=2, pady=2, sticky="NSEW")

        entree_combo.bind('<<ComboboxSelected>>', self.entree_changed)
        side_combo.bind('<<ComboboxSelected>>', self.combo_changed)
        drink_combo.bind('<<ComboboxSelected>>', self.combo_changed)

        save = Button(master=self, text="Save",
                      command=lambda:
                      self.action_performed("save"))
        save.grid(row=5, column=0, sticky="EW")

        cancel = Button(master=self, text="Cancel",
                        command=lambda:
                        self.action_performed("cancel"))
        cancel.grid(row=5, column=2, sticky="NEW")

    def load_menu_panel(self) -> None:
        """Load menu panel."""
        pass

    def save_item(self, item: Item) -> None:
        """Save item."""
        pass

    def combo_changed(self, event) -> None:
        """Combo changed event."""
        pass

    def action_performed(self, text: str) -> None:
        """Action performed method."""
        if text == "cancel":
            self.__master.load_menu_panel()
        elif text == "save":
            pass

    def entree_changed(self, event) -> None:
        # destroy existing panel if any
        # figure out which panel to load
        entree = self._entree_var.get()
        if entree == "None":
            # load a blank panel
            pass
        else:
            panel = PanelFactory.get_panel(self, name=entree) # "Clue Chili"
            self._entree_panel = panel
        self._entree_panel.grid(row=1, column=0, padx=2, pady=2, sticky="NSEW")