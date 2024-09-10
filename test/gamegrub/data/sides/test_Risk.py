"""Test Class for Risk Bites.

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

class TestRisk():
    """Test class for 'srs.gamegrub.data.sides.Risk.py'."""
    def test_size_default_is_correct(self):
        side = RiskBites()
        assert side.size == Size.JUNIOR

    def test_junior_size_price(self):
        side = RiskBites()
        side.size = Size.JUNIOR
        assert side.price == 3.95

    def test_junior_size_calories(self):
        side = RiskBites()
        side.size = Size.JUNIOR
        assert side.calories == 480

    def test_junior_size_string(self, capsys):
        side = RiskBites()
        print(side)
        captured = capsys.readouterr()
        assert captured.out == "Junior Risk Bites\n", "Unexpected Output"

    def test_classic_size_price(self):
        side = RiskBites()
        side.size = Size.CLASSIC
        assert side.price == 5.15

    def test_classic_size_calories(self):
        side = RiskBites()
        side.size = Size.CLASSIC
        assert side.calories == 755

    def test_classic_size_string(self, capsys):
        side = RiskBites()
        side.size = Size.CLASSIC
        print(side)
        captured = capsys.readouterr()
        assert captured.out == "Classic Risk Bites\n", "Unexpected Output"

    def test_winner_size_price(self):
        side = RiskBites()
        side.size = Size.WINNER
        assert side.price == 6.95

    def test_winner_size_calories(self):
        side = RiskBites()
        side.size = Size.WINNER
        assert side.calories == 940

    def test_winner_size_string(self, capsys):
        side = RiskBites()
        side.size = Size.WINNER
        print(side)
        captured = capsys.readouterr()
        assert captured.out == "Winner Risk Bites\n", "Unexpected Output"

    def test_two_instances_of_same_object_are_equal(self):
        side1 = RiskBites()
        side2 = RiskBites()
        assert side1 == side2

    def test_two_different_size_not_equal(self):
        side1 = RiskBites()
        side2 = RiskBites()
        side2.size = Size.CLASSIC
        assert not side1 == side2

    def test_two_objects_not_equal(self):
        side1 = RiskBites()
        side2 = PotatoDice()
        assert not side1 == side2