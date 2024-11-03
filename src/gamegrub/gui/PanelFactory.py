"""Panel Factory class.

Uses the Factory design pattern
to create a panel

Author: Mason Pride
Version: 0.1
"""
from src.gamegrub.data.Item import Item
from src.gamegrub.data.entrees.Chess import ChessChickenParm
from src.gamegrub.data.entrees.Clue import ClueChili
from src.gamegrub.data.entrees.Jenga import JengaNachos
from src.gamegrub.data.entrees.Monopoly import MonopolyBowl
from src.gamegrub.data.entrees.Yahtzee import YahtzeePoke
from src.gamegrub.data.drinks.Candy import CandyLandShake
from src.gamegrub.data.drinks.Cranium import CraniumCoffee
from src.gamegrub.data.drinks.Sorry import SorrySoda
from src.gamegrub.data.sides.Side import Side
from src.gamegrub.gui.sides.SidePanel import SidePanel
from src.gamegrub.gui.entrees.ChessPanel import ChessPanel
from src.gamegrub.gui.entrees.CluePanel import CluePanel
from src.gamegrub.gui.entrees.JengaPanel import JengaPanel
from src.gamegrub.gui.entrees.MonopolyPanel import MonopolyPanel
from src.gamegrub.gui.entrees.YahtzeePanel import YahtzeePanel
from src.gamegrub.data.drinks.Drink import Drink
from src.gamegrub.gui.drinks.CandyPanel import CandyPanel
from src.gamegrub.gui.drinks.CraniumPanel import CraniumPanel
from src.gamegrub.gui.drinks.SorryPanel import SorryPanel
from src.gamegrub.gui.ComboPanel import ComboPanel
from src.gamegrub.data.sides.Catan import CatanSkewers
from src.gamegrub.data.sides.Dice import PotatoDice
from src.gamegrub.data.sides.Risk import RiskBites


class PanelFactory:
    """Panel factory class."""

    @staticmethod
    def get_panel_by_item(parent, item: Item):
        """Builds the panel by item.

        Builds the wanted panel.

        Args:
            parent: Parent Frame
            item: Item desired

        Returns:
            Panel of desired item.
        """
        if isinstance(item, ChessChickenParm):
            return ChessPanel(parent, item)
        elif isinstance(item, ClueChili):
            return CluePanel(parent, item)
        elif isinstance(item, JengaNachos):
            return JengaPanel(parent, item)
        elif isinstance(item, YahtzeePoke):
            return YahtzeePanel(parent, item)
        elif isinstance(item, MonopolyBowl):
            return MonopolyPanel(parent, item)
        elif isinstance(item, CandyLandShake):
            return CandyPanel(parent, item)
        elif isinstance(item, CraniumCoffee):
            return CraniumPanel(parent, item)
        elif isinstance(item, SorrySoda):
            return SorryPanel(parent, item)
        elif isinstance(item, Side):
            return SidePanel(parent, item)

    @staticmethod
    def get_panel_by_name(parent, name: str):
        """Builds the panel by name.

        Builds the wanted panel.

        Args:
            parent: Parent Frame
            name: Name of item desired

        Returns:
            Panel of desired item.
        """
        if name == "Clue Chili":
            c = ClueChili()
            return CluePanel(parent, c)
        elif name == "Chess Chicken Parm":
            c = ChessChickenParm()
            return ChessPanel(parent, c)
        elif name == "Chess Chicken Parm":
            c = ChessChickenParm()
            return ChessPanel(parent, c)
        elif name == "Jenga Nachos":
            c = JengaNachos()
            return JengaPanel(parent, c)
        elif name == "Yahtzee Poke":
            c = YahtzeePoke()
            return YahtzeePanel(parent, c)
        elif name == "Monopoly Bowl":
            c = MonopolyBowl()
            return MonopolyPanel(parent, c)
        elif name == "Candy Land Shake":
            c = CandyLandShake()
            return CandyPanel(parent, c)
        elif name == "Cranium Coffee":
            c = CraniumCoffee()
            return CraniumPanel(parent, c)
        elif name == "Sorry Soda":
            c = SorrySoda()
            return SorryPanel(parent, c)
        elif name == "Catan Skewers":
            c = CatanSkewers()
            return SidePanel(parent, c)
        elif name == "Risk Bites":
            c = RiskBites()
            return SidePanel(parent, c)
        elif name == "Potato Dice":
            c = PotatoDice()
            return SidePanel(parent, c)
