"""Test Class for Chess Chicken Parm.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.gamegrub.data.entrees.Chess import ChessChickenParm
from src.gamegrub.data.entrees.Clue import ClueChili
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings

class TestChess():
    """Test class for 'srs.gamegrub.data.entrees.Chess.py'."""

    """when a new object is created"""
    def test_instructions_size_is_zero_on_init(self):
        entree = ChessChickenParm()
        assert len(entree.instructions) == 0

    def test_default_base_is_set_correctly(self):
        entree = ChessChickenParm()
        assert entree.base == Base.SPAGHETTI

    def test_default_toppings_set_correctly(self):
        entree = ChessChickenParm()
        correctToppings: Set[Toppings] = {Toppings.CHEESE, Toppings.FRESH_HERBS}
        assert entree.toppings == correctToppings

    def test_default_calories_is_correct(self):
        entree = ChessChickenParm()
        assert entree.calories == 1555

    """for every base"""
    def test_price_of_spaghetti_base(self):
        entree = ChessChickenParm()
        entree.base = Base.SPAGHETTI
        assert entree.price == 13.65

    def test_string_of_spaghetti_base(self, capsys):
        entree = ChessChickenParm()
        entree.base = Base.SPAGHETTI
        print(entree)
        captured = capsys.readouterr()
        assert captured.out == "Chess Chicken Parm on Spaghetti\n", "Unexpected Output"

    def test_price_of_rice_base(self):
        entree = ChessChickenParm()
        entree.base = Base.RICE
        assert entree.price == 13.15

    def test_string_of_rice_base(self, capsys):
        entree = ChessChickenParm()
        entree.base = Base.RICE
        print(entree)
        captured = capsys.readouterr()
        assert captured.out == "Chess Chicken Parm on Rice\n", "Unexpected Output"

    def test_price_of_chips_base(self):
        entree = ChessChickenParm()
        entree.base = Base.CHIPS
        assert entree.price == 14.15

    def test_string_of_chips_base(self, capsys):
        entree = ChessChickenParm()
        entree.base = Base.CHIPS
        print(entree)
        captured = capsys.readouterr()
        assert captured.out == "Chess Chicken Parm on Chips\n", "Unexpected Output"

    """for every ingredient"""
    def test_crispy_chicken_true_on_default(self):
        entree = ChessChickenParm()
        assert entree.crispy_chicken == True

    def test_red_sauce_true_on_default(self):
        entree = ChessChickenParm()
        assert entree.red_sauce == True

    def test_remove_crispy_chicken_adds_to_instructions(self):
        entree = ChessChickenParm()
        entree.crispy_chicken = False
        assert len(entree.instructions) == 1

    def test_remove_red_sauce_adds_to_instructions(self):
        entree = ChessChickenParm()
        entree.red_sauce = False
        assert len(entree.instructions) == 1

    """for every topping"""
    def test_removing_fresh_herbs_removes_from_toppings(self):
        entree = ChessChickenParm()
        entree.remove_topping(Toppings.FRESH_HERBS)
        correctToppings: Set[Toppings] = {Toppings.CHEESE}
        assert entree.toppings == correctToppings

    def test_removing_cheese_removes_from_toppings(self):
        entree = ChessChickenParm()
        entree.remove_topping(Toppings.CHEESE)
        correctToppings: Set[Toppings] = {Toppings.FRESH_HERBS}
        assert entree.toppings == correctToppings

    @pytest.mark.parametrize("topping", [Toppings.ONIONS, Toppings.SOY_SAUCE, Toppings.HOT_SAUCE])
    def test_adding_toppings_to_entree(self, topping):
        entree = ChessChickenParm()
        entree.add_topping(topping)
        correctToppings: Set[Toppings] = {Toppings.CHEESE, Toppings.FRESH_HERBS, topping}
        assert entree.toppings == correctToppings

    @pytest.mark.parametrize("topping", [Toppings.ONIONS, Toppings.SOY_SAUCE, Toppings.HOT_SAUCE])
    def test_removing_toppings_removes_from_topping_list(self, topping):
        entree = ChessChickenParm()
        entree.add_topping(topping)
        entree.remove_topping(topping)
        correctToppings: Set[Toppings] = {Toppings.CHEESE, Toppings.FRESH_HERBS}
        assert entree.toppings == correctToppings

    """equality tests"""
    def test_two_instances_of_same_object_are_equal(self):
        entree1 = ChessChickenParm()
        entree2 = ChessChickenParm()
        assert entree1 == entree2

    def test_two_instances_with_different_bases(self):
        entree1 = ChessChickenParm()
        entree2 = ChessChickenParm()
        entree2.base = Base.CHIPS
        assert not entree1 == entree2
    
    def test_two_instances_with_different_ingredients(self):
        entree1 = ChessChickenParm()
        entree2 = ChessChickenParm()
        entree2.red_sauce = False
        assert not entree1 == entree2
    
    def test_two_instances_with_different_toppings(self):
        entree1 = ChessChickenParm()
        entree2 = ChessChickenParm()
        entree2.add_topping(Toppings.ONIONS)
        assert not entree1 == entree2

    def test_two_different_objects(self):
        entree1 = ChessChickenParm()
        entree2 = ClueChili()
        assert not entree1 == entree2
