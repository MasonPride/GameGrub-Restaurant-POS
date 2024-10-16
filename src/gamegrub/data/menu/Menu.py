"""Static class of menu.

Author: Mason Pride
version: 0.1
"""

from src.gamegrub.data.Item import Item
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
from src.gamegrub.data.combo.ComboBuilder import ComboBuilder
from typing import List


class Menu():
    """Menu class.

    Class containing all menu items.
    """
    @staticmethod
    def entrees() -> List[Item]:
        """Entrees getter method.

        Displays all entree items

        Returns:
            List of Item elements of all entrees
        """
        entree_list: List[Item] = []
        chess = ChessChickenParm()
        entree_list.append(chess)
        clue = ClueChili()
        entree_list.append(clue)
        jenga = JengaNachos()
        entree_list.append(jenga)
        monopoly = MonopolyBowl()
        entree_list.append(monopoly)
        yahtzee = YahtzeePoke()
        entree_list.append(yahtzee)
        return entree_list

    @staticmethod
    def drinks() -> List[Item]:
        """Drinks getter method.

        Displays all drink items

        Returns:
            List of Item elements of all drinks
        """
        drink_list: List[Item] = []
        candy_j = CandyLandShake()
        candy_c = CandyLandShake()
        candy_c.size = Size.CLASSIC
        candy_w = CandyLandShake()
        candy_w.size = Size.WINNER
        drink_list.append(candy_j)
        drink_list.append(candy_c)
        drink_list.append(candy_w)
        cranium_j = CraniumCoffee()
        cranium_c = CraniumCoffee()
        cranium_c.size = Size.CLASSIC
        cranium_w = CraniumCoffee()
        cranium_w.size = Size.WINNER
        drink_list.append(cranium_j)
        drink_list.append(cranium_c)
        drink_list.append(cranium_w)
        sorry_j = SorrySoda()
        sorry_c = SorrySoda()
        sorry_c.size = Size.CLASSIC
        sorry_w = SorrySoda()
        sorry_w.size = Size.WINNER
        drink_list.append(sorry_j)
        drink_list.append(sorry_c)
        drink_list.append(sorry_w)
        return drink_list

    @staticmethod
    def sides() -> List[Item]:
        """Sides getter method.

        Displays all side items

        Returns:
            List of Item elements of all sides
        """
        side_list: List[Item] = []
        catan_j = CatanSkewers()
        catan_c = CatanSkewers()
        catan_c.size = Size.CLASSIC
        catan_w = CatanSkewers()
        catan_w.size = Size.WINNER
        side_list.append(catan_j)
        side_list.append(catan_c)
        side_list.append(catan_w)
        potato_j = PotatoDice()
        potato_c = PotatoDice()
        potato_c.size = Size.CLASSIC
        potato_w = PotatoDice()
        potato_w.size = Size.WINNER
        side_list.append(potato_j)
        side_list.append(potato_c)
        side_list.append(potato_w)
        risk_j = RiskBites()
        risk_c = RiskBites()
        risk_c.size = Size.CLASSIC
        risk_w = RiskBites()
        risk_w.size = Size.WINNER
        side_list.append(risk_j)
        side_list.append(risk_c)
        side_list.append(risk_w)
        return side_list

    @staticmethod
    def combos() -> List[Item]:
        """Combos getter.

        Returns:
            List of items representing all combos
        """
        combos: List[Item] = []
        game_night = ComboBuilder().build_combo("Game Night")
        combos.append(game_night)
        roll_the_dice = ComboBuilder().build_combo("Roll the Dice")
        combos.append(roll_the_dice)
        big_appetite = ComboBuilder().build_combo("Big Appetite")
        combos.append(big_appetite)
        the_winner = ComboBuilder().build_combo("The Winner")
        combos.append(the_winner)
        return combos

    def fullmenu(self) -> List[Item]:
        """Represents full menu.

        Returns:
            List of items representing the whole menu.
        """
        entrees = self.entrees()
        drinks = self.drinks()
        sides = self.sides()
        combos = self.combos()
        full_menu = entrees + drinks + sides + combos
        return full_menu
