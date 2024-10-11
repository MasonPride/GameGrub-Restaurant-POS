"""Test Class for Menu.py.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.gamegrub.data.menu.Menu import Menu
from src.gamegrub.data.combo.Combo import Combo
from src.gamegrub.data.combo.ComboBuilder import ComboBuilder

class TestMenu():
    """Test class for 'srs.gamegrub.data.menu.Menu.py."""
    def test_menu_contains_game_night(self):
        menu = Menu()
        menu_combos = menu.combos()
        game_night: Combo() = ComboBuilder().build_combo("Game Night")
        assert game_night in menu_combos

    def test_menu_contains_roll_the_dice(self):
        menu = Menu()
        menu_combos = menu.combos()
        game_night: Combo() = ComboBuilder().build_combo("Roll the Dice")
        assert game_night in menu_combos

    def test_menu_contains_big_appetite(self):
        menu = Menu()
        menu_combos = menu.combos()
        game_night: Combo() = ComboBuilder().build_combo("Big Appetite")
        assert game_night in menu_combos

    def test_menu_contains_the_winner(self):
        menu = Menu()
        menu_combos = menu.combos()
        game_night: Combo() = ComboBuilder().build_combo("The Winner")
        assert game_night in menu_combos

    