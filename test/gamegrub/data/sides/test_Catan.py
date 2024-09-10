"""Test Class for Catan Skewers.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.gamegrub.data.sides.Risk import RiskBites
from src.gamegrub.data.sides.Catan import CatanSkewers
from src.gamegrub.data.enums.Size import Size

class TestCatan():
    """Test class for 'srs.gamegrub.data.sides.Catan.py'."""
    def test_size_default_is_correct(self):
        side = CatanSkewers()
        assert side.size == Size.JUNIOR

    def test_junior_size_price(self):
        side = CatanSkewers()
        side.size = Size.JUNIOR
        assert side.price == 4.45

    def test_junior_size_calories(self):
        side = CatanSkewers()
        side.size = Size.JUNIOR
        assert side.calories == 530

    def test_junior_size_string(self, capsys):
        side = CatanSkewers()
        print(side)
        captured = capsys.readouterr()
        assert captured.out == "Junior Catan Skewers\n", "Unexpected Output"

    def test_classic_size_price(self):
        side = CatanSkewers()
        side.size = Size.CLASSIC
        assert side.price == 6.85

    def test_classic_size_calories(self):
        side = CatanSkewers()
        side.size = Size.CLASSIC
        assert side.calories == 815

    def test_classic_size_string(self, capsys):
        side = CatanSkewers()
        side.size = Size.CLASSIC
        print(side)
        captured = capsys.readouterr()
        assert captured.out == "Classic Catan Skewers\n", "Unexpected Output"

    def test_winner_size_price(self):
        side = CatanSkewers()
        side.size = Size.WINNER
        assert side.price == 8.65

    def test_winner_size_calories(self):
        side = CatanSkewers()
        side.size = Size.WINNER
        assert side.calories == 1045

    def test_winner_size_string(self, capsys):
        side = CatanSkewers()
        side.size = Size.WINNER
        print(side)
        captured = capsys.readouterr()
        assert captured.out == "Winner Catan Skewers\n", "Unexpected Output"

    def test_two_instances_of_same_object_are_equal(self):
        side1 = CatanSkewers()
        side2 = CatanSkewers()
        assert side1 == side2

    def test_two_different_size_not_equal(self):
        side1 =CatanSkewers()
        side2 = CatanSkewers()
        side2.size = Size.CLASSIC
        assert not side1 == side2

    def test_two_objects_not_equal(self):
        side1 = CatanSkewers()
        side2 = RiskBites()
        assert not side1 == side2