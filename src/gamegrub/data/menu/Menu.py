"""Static class of menu.

Author: Mason Pride
version: 0.1
"""

from src.gamegrub.data.Item import Item
from src.gamegrub.data.enums.Toppings import Toppings
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Size import Size
from src.gamegrub.data.entrees.Chess import ChessChickenParm
from src.gamegrub.data.entrees.Clue import ClueChili
from src.gamegrub.data.entrees.Jenga import JengaNachos
from src.gamegrub.data.entrees.Monopoly import MonopolyBowl
from src.gamegrub.data.entrees.Yahtzee import YahtzeePoke
from src.gamegrub.data.drinks.Candy import CandyLandShake
from src.gamegrub.data.drinks.Cranium import CraniumCoffee
from src.gamegrub.data.drinks.Sorry import SorrySoda
from src.gamegrub.data.sides.Catan import CatanSkewers
from src.gamegrub.data.sides.Dice import PotatoDice
from src.gamegrub.data.sides.Risk import RiskBites
from typing import List


class Menu():
    """Menu class.

    Class containing all menu items.
    """
    def entrees(self) -> List[Item]:
        """entrees getter method.

        Displays all entree items

        Returns:
            List of Item elements of all entrees
        """
        entreeList: List[Item] = []
        chess = ChessChickenParm()
        entreeList.append(chess)
        clue = ClueChili()
        entreeList.append(clue)
        jenga = JengaNachos()
        entreeList.append(jenga)
        monopoly = MonopolyBowl()
        entreeList.append(monopoly)
        yahtzee = YahtzeePoke()
        entreeList.append(yahtzee)
        return entreeList

    def drinks(self) -> List[Item]:
        """drinks getter method.

        Displays all drink items

        Returns:
            List of Item elements of all drinks
        """
        drinkList: List[Item] = []
        candyJ = CandyLandShake()
        candyC = CandyLandShake()
        candyC.size = Size.CLASSIC
        candyW = CandyLandShake()
        candyW.size = Size.WINNER
        drinkList.append(candyJ)
        drinkList.append(candyC)
        drinkList.append(candyW)
        craniumJ = CraniumCoffee()
        craniumC = CraniumCoffee()
        craniumC.size = Size.CLASSIC
        craniumW = CraniumCoffee()
        craniumW.size = Size.WINNER
        drinkList.append(craniumJ)
        drinkList.append(craniumC)
        drinkList.append(craniumW)
        sorryJ = SorrySoda()
        sorryC = SorrySoda()
        sorryC.size = Size.CLASSIC
        sorryW = SorrySoda()
        sorryW.size = Size.WINNER
        drinkList.append(sorryJ)
        drinkList.append(sorryC)
        drinkList.append(sorryW)
        return drinkList

    def sides(self) -> List[Item]:
        """sides getter method.

        Displays all side items

        Returns:
            List of Item elements of all sides
        """
        sideList: List[Item] = []
        catanJ = CatanSkewers()
        catanC = CatanSkewers()
        catanC.size = Size.CLASSIC
        catanW = CatanSkewers()
        catanW.size = Size.WINNER
        sideList.append(catanJ)
        sideList.append(catanC)
        sideList.append(catanW)
        potatoJ = PotatoDice()
        potatoC = PotatoDice()
        potatoC.size = Size.CLASSIC
        potatoW = PotatoDice()
        potatoW.size = Size.WINNER
        sideList.append(potatoJ)
        sideList.append(potatoC)
        sideList.append(potatoW)
        riskJ = RiskBites()
        riskC = RiskBites()
        riskC.size = Size.CLASSIC
        riskW = RiskBites()
        riskW.size = Size.WINNER
        sideList.append(riskJ)
        sideList.append(riskC)
        sideList.append(riskW)
        return sideList

    def fullmenu(self) -> List[Item]:
        entrees = self.entrees()
        drinks = self.drinks()
        sides = self.sides()
        fullMenu = entrees + drinks + sides
        return fullMenu