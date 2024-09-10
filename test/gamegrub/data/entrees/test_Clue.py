"""Test Class for Clue Chili.

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

class TestClue():
    """Test class for 'srs.gamegrub.data.entrees.Clue.py'."""

    def test_instructions_size_is_zero_on_init(self):
        entree = ClueChili()
        assert len(entree.instructions) == 0

    def test_default_base_is_set_correctly(self):
        entree = ClueChili()
        assert entree.base == Base.SPAGHETTI

    def test_default_toppings_set_correctly(self):
        entree = ClueChili()
        correctToppings: Set[Toppings] = {Toppings.CHEESE, Toppings.ONIONS, Toppings.HOT_SAUCE}
        assert entree.toppings == correctToppings

    def test_default_calories_is_correct(self):
        entree = ClueChili()
        assert entree.calories == 1165

    def test_price_of_spaghetti_base(self):
        entree = ClueChili()
        entree.base = Base.SPAGHETTI
        assert entree.price == 10.45

    def test_string_of_spaghetti_base(self, capsys):
        entree = ClueChili()
        entree.base = Base.SPAGHETTI
        print(entree)
        captured = capsys.readouterr()
        assert captured.out == "Clue Chili on Spaghetti\n", "Unexpected Output"

    def test_price_of_rice_base(self):
        entree = ClueChili()
        entree.base = Base.RICE
        assert entree.price == 9.95

    def test_string_of_rice_base(self, capsys):
        entree = ClueChili()
        entree.base = Base.RICE
        print(entree)
        captured = capsys.readouterr()
        assert captured.out == "Clue Chili on Rice\n", "Unexpected Output"

    def test_price_of_chips_base(self):
        entree = ClueChili()
        entree.base = Base.CHIPS
        assert entree.price == 10.95

    def test_string_of_chips_base(self, capsys):
        entree = ClueChili()
        entree.base = Base.CHIPS
        print(entree)
        captured = capsys.readouterr()
        assert captured.out == "Clue Chili on Chips\n", "Unexpected Output"
    
    def test_spicy_beef_true_on_default(self):
        entree = ClueChili()
        assert entree.spicy_beef == True
    
    def test_remove_spicy_beef_adds_to_instructions(self):
        entree = ClueChili()
        entree.spicy_beef = False
        assert len(entree.instructions) == 1

    def test_red_sauce_true_on_default(self):
        entree = ClueChili()
        assert entree.red_sauce == True

    def test_remove_red_sauce_adds_to_instructions(self):
        entree = ClueChili()
        entree.red_sauce = False
        assert len(entree.instructions) == 1
    
    def test_chili_true_on_default(self):
        entree = ClueChili()
        assert entree.chili == True
    
    def test_remove_chili_adds_to_instructions(self):
        entree = ClueChili()
        entree.chili = False
        assert len(entree.instructions) == 1
    
    def test_beans_true_on_default(self):
        entree = ClueChili()
        assert entree.beans == True
    
    def test_remove_beans_adds_to_instructions(self):
        entree = ClueChili()
        entree.beans = False
        assert len(entree.instructions) == 1
    
    def test_removing_onions_removes_from_toppings(self):
        entree = ClueChili()
        entree.remove_topping(Toppings.ONIONS)
        correctToppings: Set[Toppings] = {Toppings.CHEESE, Toppings.HOT_SAUCE}
        assert entree.toppings == correctToppings

    def test_removing_cheese_removes_from_toppings(self):
        entree = ClueChili()
        entree.remove_topping(Toppings.CHEESE)
        correctToppings: Set[Toppings] = {Toppings.ONIONS, Toppings.HOT_SAUCE}
        assert entree.toppings == correctToppings
    
    def test_removing_hot_sauce_removes_from_toppings(self):
        entree = ClueChili()
        entree.remove_topping(Toppings.HOT_SAUCE)
        correctToppings: Set[Toppings] = {Toppings.ONIONS, Toppings.CHEESE}
        assert entree.toppings == correctToppings

    @pytest.mark.parametrize("topping", [Toppings.SOUR_CREAM, Toppings.SOY_SAUCE, Toppings.FRESH_HERBS])
    def test_adding_toppings_to_entree(self, topping):
        entree = ClueChili()
        entree.add_topping(topping)
        correctToppings: Set[Toppings] = {Toppings.CHEESE, Toppings.ONIONS, Toppings.HOT_SAUCE, topping}
        assert entree.toppings == correctToppings

    @pytest.mark.parametrize("topping", [Toppings.SOUR_CREAM, Toppings.SOY_SAUCE, Toppings.FRESH_HERBS])
    def test_removing_toppings_removes_from_topping_list(self, topping):
        entree = ClueChili()
        entree.add_topping(topping)
        entree.remove_topping(topping)
        correctToppings: Set[Toppings] = {Toppings.ONIONS, Toppings.CHEESE, Toppings.HOT_SAUCE}
        assert entree.toppings == correctToppings

    def test_two_instances_of_same_object_are_equal(self):
        entree1 = ClueChili()
        entree2 = ClueChili()
        assert entree1 == entree2

    def test_two_instances_with_different_bases(self):
        entree1 = ClueChili()
        entree2 = ClueChili()
        entree2.base = Base.CHIPS
        assert not entree1 == entree2
    
    def test_two_instances_with_different_ingredients(self):
        entree1 = ClueChili()
        entree2 = ClueChili()
        entree2.spicy_beef = False
        assert not entree1 == entree2
    
    def test_two_instances_with_different_toppings(self):
        entree1 = ClueChili()
        entree2 = ClueChili()
        entree2.add_topping(Toppings.SOUR_CREAM)
        assert not entree1 == entree2

    def test_two_different_objects(self):
        entree1 = ChessChickenParm()
        entree2 = ClueChili()
        assert not entree2 == entree1
