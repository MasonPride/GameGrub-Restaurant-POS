"""Test Class for Jenga Nachos.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.gamegrub.data.entrees.Jenga import JengaNachos
from src.gamegrub.data.entrees.Clue import ClueChili
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings

class TestJenga():
    """Test class for 'srs.gamegrub.data.entrees.Jenga.py'."""

    def test_instructions_size_is_zero_on_init(self):
        entree = JengaNachos()
        assert len(entree.instructions) == 0

    def test_default_base_is_set_correctly(self):
        entree = JengaNachos()
        assert entree.base == Base.CHIPS

    def test_default_toppings_set_correctly(self):
        entree = JengaNachos()
        correctToppings: Set[Toppings] = {
            Toppings.CHEESE, Toppings.ONIONS, Toppings.SOUR_CREAM,
            Toppings.HOT_SAUCE, Toppings.GUACAMOLE}
        assert entree.toppings == correctToppings

    def test_default_calories_is_correct(self):
        entree = JengaNachos()
        assert entree.calories == 1470

    def test_price_of_spaghetti_base(self):
        entree = JengaNachos()
        entree.base = Base.SPAGHETTI
        assert entree.price == 11.35

    def test_string_of_spaghetti_base(self, capsys):
        entree = JengaNachos()
        entree.base = Base.SPAGHETTI
        print(entree)
        captured = capsys.readouterr()
        assert captured.out == "Jenga Nachos on Spaghetti\n", "Unexpected Output"

    def test_price_of_rice_base(self):
        entree = JengaNachos()
        entree.base = Base.RICE
        assert entree.price == 10.85

    def test_string_of_rice_base(self, capsys):
        entree = JengaNachos()
        entree.base = Base.RICE
        print(entree)
        captured = capsys.readouterr()
        assert captured.out == "Jenga Nachos on Rice\n", "Unexpected Output"

    def test_price_of_chips_base(self):
        entree = JengaNachos()
        entree.base = Base.CHIPS
        assert entree.price == 11.85

    def test_string_of_chips_base(self, capsys):
        entree = JengaNachos()
        entree.base = Base.CHIPS
        print(entree)
        captured = capsys.readouterr()
        assert captured.out == "Jenga Nachos on Chips\n", "Unexpected Output"
    
    def test_spicy_beef_true_on_default(self):
        entree = JengaNachos()
        assert entree.spicy_beef == True
    
    def test_remove_spicy_beef_adds_to_instructions(self):
        entree = JengaNachos()
        entree.spicy_beef = False
        assert len(entree.instructions) == 1
    
    def test_beans_true_on_default(self):
        entree = JengaNachos()
        assert entree.beans == True
    
    def test_remove_beans_adds_to_instructions(self):
        entree = JengaNachos()
        entree.beans = False
        assert len(entree.instructions) == 1
    
    def test_removing_onions_removes_from_toppings(self):
        entree = JengaNachos()
        entree.remove_topping(Toppings.ONIONS)
        correctToppings: Set[Toppings] = {
            Toppings.CHEESE, Toppings.SOUR_CREAM,
            Toppings.HOT_SAUCE, Toppings.GUACAMOLE}
        assert entree.toppings == correctToppings
    
    def test_removing_cheese_removes_from_toppings(self):
        entree = JengaNachos()
        entree.remove_topping(Toppings.CHEESE)
        correctToppings: Set[Toppings] = {
            Toppings.ONIONS, Toppings.SOUR_CREAM,
            Toppings.HOT_SAUCE, Toppings.GUACAMOLE}
        assert entree.toppings == correctToppings

    def test_removing_hot_sauce_removes_from_toppings(self):
        entree = JengaNachos()
        entree.remove_topping(Toppings.HOT_SAUCE)
        correctToppings: Set[Toppings] = {
            Toppings.CHEESE, Toppings.ONIONS, Toppings.SOUR_CREAM,
            Toppings.GUACAMOLE}
        assert entree.toppings == correctToppings
    
    def test_removing_sour_cream_removes_from_toppings(self):
        entree = JengaNachos()
        entree.remove_topping(Toppings.SOUR_CREAM)
        correctToppings: Set[Toppings] = {
            Toppings.CHEESE, Toppings.ONIONS, Toppings.HOT_SAUCE,
            Toppings.GUACAMOLE}
        assert entree.toppings == correctToppings

    def test_removing_guacamole_removes_from_toppings(self):
        entree = JengaNachos()
        entree.remove_topping(Toppings.GUACAMOLE)
        correctToppings: Set[Toppings] = {
            Toppings.CHEESE, Toppings.ONIONS, Toppings.HOT_SAUCE,
            Toppings.SOUR_CREAM}
        assert entree.toppings == correctToppings

    @pytest.mark.parametrize("topping", [Toppings.SOUR_CREAM, Toppings.SOY_SAUCE, Toppings.FRESH_HERBS])
    def test_adding_toppings_to_entree(self, topping):
        entree = JengaNachos()
        entree.add_topping(topping)
        correctToppings: Set[Toppings] = {
            Toppings.CHEESE, Toppings.ONIONS, Toppings.SOUR_CREAM,
            Toppings.HOT_SAUCE, Toppings.GUACAMOLE, topping}
        assert entree.toppings == correctToppings

    @pytest.mark.parametrize("topping", [Toppings.CRISPY_STRIPS, Toppings.SOY_SAUCE, Toppings.FRESH_HERBS])
    def test_removing_toppings_removes_from_topping_list(self, topping):
        entree = JengaNachos()
        entree.add_topping(topping)
        entree.remove_topping(topping)
        correctToppings: Set[Toppings] = {Toppings.CHEESE, Toppings.ONIONS, Toppings.SOUR_CREAM,
            Toppings.HOT_SAUCE, Toppings.GUACAMOLE}
        assert entree.toppings == correctToppings

    def test_two_instances_of_same_object_are_equal(self):
        entree1 = JengaNachos()
        entree2 = JengaNachos()
        assert entree1 == entree2

    def test_two_instances_with_different_bases(self):
        entree1 = JengaNachos()
        entree2 = JengaNachos()
        entree2.base = Base.SPAGHETTI
        assert not entree1 == entree2
    
    def test_two_instances_with_different_ingredients(self):
        entree1 = JengaNachos()
        entree2 = JengaNachos()
        entree2.spicy_beef = False
        assert not entree1 == entree2
    
    def test_two_instances_with_different_toppings(self):
        entree1 = JengaNachos()
        entree2 = JengaNachos()
        entree2.add_topping(Toppings.FRESH_HERBS)
        assert not entree1 == entree2

    def test_two_different_objects(self):
        entree1 = JengaNachos()
        entree2 = ClueChili()
        assert not entree1 == entree2
