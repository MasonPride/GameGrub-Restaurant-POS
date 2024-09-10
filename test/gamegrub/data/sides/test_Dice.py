"""Test Class for Potato Dice.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.gamegrub.data.sides.Risk import RiskBites
from src.gamegrub.data.sides.Dice import PotatoDice
from src.gamegrub.data.enums.Size import Size

class TestDice():
    """Test class for 'srs.gamegrub.data.sides.Dice.py'."""
    def test_size_default_is_correct(self):
        side = PotatoDice()
        assert side.size == Size.JUNIOR

    def test_junior_size_price(self):
        side = PotatoDice()
        side.size = Size.JUNIOR
        assert side.price == 2.75

    def test_junior_size_calories(self):
        side = PotatoDice()
        side.size = Size.JUNIOR
        assert side.calories == 350

    def test_junior_size_string(self, capsys):
        side = PotatoDice()
        print(side)
        captured = capsys.readouterr()
        assert captured.out == "Junior Potato Dice\n", "Unexpected Output"

    def test_classic_size_price(self):
        side = PotatoDice()
        side.size = Size.CLASSIC
        assert side.price == 3.85

    def test_classic_size_calories(self):
        side = PotatoDice()
        side.size = Size.CLASSIC
        assert side.calories == 475

    def test_classic_size_string(self, capsys):
        side = PotatoDice()
        side.size = Size.CLASSIC
        print(side)
        captured = capsys.readouterr()
        assert captured.out == "Classic Potato Dice\n", "Unexpected Output"

    def test_winner_size_price(self):
        side = PotatoDice()
        side.size = Size.WINNER
        assert side.price == 5.35

    def test_winner_size_calories(self):
        side = PotatoDice()
        side.size = Size.WINNER
        assert side.calories == 795

    def test_winner_size_string(self, capsys):
        side = PotatoDice()
        side.size = Size.WINNER
        print(side)
        captured = capsys.readouterr()
        assert captured.out == "Winner Potato Dice\n", "Unexpected Output"

    def test_two_instances_of_same_object_are_equal(self):
        side1 = PotatoDice()
        side2 = PotatoDice()
        assert side1 == side2

    def test_two_different_size_not_equal(self):
        side1 = PotatoDice()
        side2 = PotatoDice()
        side2.size = Size.CLASSIC
        assert not side1 == side2

    def test_two_objects_not_equal(self):
        side1 = PotatoDice()
        side2 = RiskBites()
        assert not side1 == side2