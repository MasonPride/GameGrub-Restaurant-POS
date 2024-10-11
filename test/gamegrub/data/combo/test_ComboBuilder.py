"""Test Class for Combo.py.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.gamegrub.data.combo.Combo import Combo
from src.gamegrub.data.combo.ComboBuilder import ComboBuilder
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


class TestComboBuilder():
    """Test class for 'srs.gamegrub.data.combo.ComboBuilder.py."""
    def test_game_night_created_correctly(self):
        """Game Night Test.

        Checks that the game night combo
        is created correctly.
        """
        combo: Combo = ComboBuilder().build_combo("Game Night")
        assert combo.name == "Game Night"
        assert combo.entree == JengaNachos()
        assert combo.side == CatanSkewers()
        assert combo.drink == SorrySoda()
    
    def test_roll_the_dice_created_correctly(self):
        """Roll the Dice Test.

        Checks that the roll the dice combo
        is created correctly.
        """
        combo: Combo = ComboBuilder().build_combo("Roll the Dice")
        assert combo.name == "Roll the Dice"
        assert combo.entree == YahtzeePoke()
        assert combo.side == PotatoDice()
        assert combo.drink == CandyLandShake()

    def test_big_appetite_created_correctly(self):
        """Big Appetite Test.

        Checks that the Big Appetite combo
        is created correctly.
        """
        combo: Combo = ComboBuilder().build_combo("Big Appetite")
        assert combo.name == "Big Appetite"
        assert combo.entree == ChessChickenParm()
        assert combo.side == RiskBites()
        assert combo.drink == CraniumCoffee()

    def test_the_winner_created_correctly(self):
        """The Winner Test.

        Checks that the The Winnner combo
        is created correctly.
        """
        combo: Combo = ComboBuilder().build_combo("The Winner")
        assert combo.name == "The Winner"
        assert combo.entree == MonopolyBowl()
        assert combo.side == PotatoDice()
        assert combo.drink == SorrySoda()

    """
    def test_invalid_name_throws_exception(self):
        pass
    """