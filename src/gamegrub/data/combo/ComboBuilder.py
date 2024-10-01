"""ComboBuilder class.

This class acts as the Builder and
Factory in our design pattern

Author: Mason Pride
Version: 0.1
"""
from src.gamegrub.data.combo.Combo import Combo
from src.gamegrub.data.entrees.Chess import ChessChickenParm
from src.gamegrub.data.entrees.Jenga import JengaNachos
from src.gamegrub.data.entrees.Monopoly import MonopolyBowl
from src.gamegrub.data.entrees.Yahtzee import YahtzeePoke
from src.gamegrub.data.drinks.Candy import CandyLandShake
from src.gamegrub.data.drinks.Cranium import CraniumCoffee
from src.gamegrub.data.drinks.Sorry import SorrySoda
from src.gamegrub.data.sides.Catan import CatanSkewers
from src.gamegrub.data.sides.Dice import PotatoDice
from src.gamegrub.data.sides.Risk import RiskBites


class ComboBuilder:
    """Combo Builder class."""

    _number_of_combos: int = 4

    @staticmethod
    def build_combo(name: str) -> Combo:
        """Combo Builder.

        Builds the combo desired by the name.

        Args:
            name: string representing the combo

        Returns:
            Combo object of the desired combo
        """
        if name == "Game Night":
            # JengaNachos , CatanSkewers , SorrySoda
            combo = Combo(name)
            combo.entree = JengaNachos()
            combo.drink = SorrySoda()
            combo.side = CatanSkewers()
            return combo
        elif name == "Roll the Dice":
            # YahtzeePoke , PotatoDice , CandyLandShake
            combo = Combo(name)
            combo.entree = YahtzeePoke()
            combo.drink = CandyLandShake()
            combo.side = PotatoDice()
            return combo
        elif name == "Big Appetite":
            # ChessChickenParm , RiskBites , CraniumCoffee
            combo = Combo(name)
            combo.entree = ChessChickenParm()
            combo.drink = CraniumCoffee()
            combo.side = RiskBites()
            return combo
        elif name == "The Winner":
            # MonopolyBowl , PotatoDice , SorrySoda
            combo = Combo(name)
            combo.entree = MonopolyBowl()
            combo.drink = SorrySoda()
            combo.side = PotatoDice()
            return combo

        @classmethod
        def number_of_combos(cls) -> int:
            """Getter for number of number combos.

            Gets the number of avaliable combos.

            Returns:
                int representing the number of combos
            """
            return cls._number_of_combos
