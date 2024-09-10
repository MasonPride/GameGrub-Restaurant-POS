"""Test Class for Yahtzee Poke.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.gamegrub.data.entrees.Yahtzee import YahtzeePoke
from src.gamegrub.data.entrees.Clue import ClueChili
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings

class TestYahtzee():
    """Test class for 'srs.gamegrub.data.entrees.Yahtzee.py'."""

    def test_instructions_size_is_zero_on_init(self):
        entree = YahtzeePoke()
        assert len(entree.instructions) == 0

    def test_default_base_is_set_correctly(self):
        entree = YahtzeePoke()
        assert entree.base == Base.RICE

    def test_default_toppings_set_correctly(self):
        entree = YahtzeePoke()
        correctToppings: Set[Toppings] = {
            Toppings.GUACAMOLE, Toppings.SOY_SAUCE, 
            Toppings.HOT_SAUCE, Toppings.CRISPY_STRIPS}
        assert entree.toppings == correctToppings

    def test_default_calories_is_correct(self):
        entree = YahtzeePoke()
        assert entree.calories == 785

    def test_price_of_spaghetti_base(self):
        entree = YahtzeePoke()
        entree.base = Base.SPAGHETTI
        assert entree.price == 15.75

    def test_string_of_spaghetti_base(self, capsys):
        entree = YahtzeePoke()
        entree.base = Base.SPAGHETTI
        print(entree)
        captured = capsys.readouterr()
        assert captured.out == "Yahtzee Poke on Spaghetti\n", "Unexpected Output"

    def test_price_of_rice_base(self):
        entree = YahtzeePoke()
        entree.base = Base.RICE
        assert entree.price == 15.25

    def test_string_of_rice_base(self, capsys):
        entree = YahtzeePoke()
        entree.base = Base.RICE
        print(entree)
        captured = capsys.readouterr()
        assert captured.out == "Yahtzee Poke on Rice\n", "Unexpected Output"

    def test_price_of_chips_base(self):
        entree = YahtzeePoke()
        entree.base = Base.CHIPS
        assert entree.price == 16.25

    def test_string_of_chips_base(self, capsys):
        entree = YahtzeePoke()
        entree.base = Base.CHIPS
        print(entree)
        captured = capsys.readouterr()
        assert captured.out == "Yahtzee Poke on Chips\n", "Unexpected Output"
    
    def test_tuna_true_on_default(self):
        entree = YahtzeePoke()
        assert entree.tuna == True
    
    def test_remove_tuna_adds_to_instructions(self):
        entree = YahtzeePoke()
        entree.tuna = False
        assert len(entree.instructions) == 1

    def test_veggies_true_on_default(self):
        entree = YahtzeePoke()
        assert entree.veggies == True

    def test_remove_veggies_adds_to_instructions(self):
        entree = YahtzeePoke()
        entree.veggies = False
        assert len(entree.instructions) == 1
    
    def test_seaweed_true_on_default(self):
        entree = YahtzeePoke()
        assert entree.seaweed == True
    
    def test_remove_seaweed_adds_to_instructions(self):
        entree = YahtzeePoke()
        entree.seaweed = False
        assert len(entree.instructions) == 1
    
    def test_removing_guacamole_removes_from_toppings(self):
        entree = YahtzeePoke()
        entree.remove_topping(Toppings.GUACAMOLE)
        correctToppings: Set[Toppings] = {
            Toppings.SOY_SAUCE, Toppings.HOT_SAUCE, Toppings.CRISPY_STRIPS}
        assert entree.toppings == correctToppings
    
    def test_removing_soy_sauce_removes_from_toppings(self):
        entree = YahtzeePoke()
        entree.remove_topping(Toppings.SOY_SAUCE)
        correctToppings: Set[Toppings] = {
            Toppings.GUACAMOLE, Toppings.HOT_SAUCE, Toppings.CRISPY_STRIPS}
        assert entree.toppings == correctToppings
    
    def test_removing_hot_sauce_removes_from_toppings(self):
        entree = YahtzeePoke()
        entree.remove_topping(Toppings.HOT_SAUCE)
        correctToppings: Set[Toppings] = {
            Toppings.GUACAMOLE, Toppings.SOY_SAUCE, 
            Toppings.CRISPY_STRIPS}
        assert entree.toppings == correctToppings

    @pytest.mark.parametrize("topping", [Toppings.SOUR_CREAM, Toppings.ONIONS, Toppings.FRESH_HERBS])
    def test_adding_toppings_to_entree(self, topping):
        entree = YahtzeePoke()
        entree.add_topping(topping)
        correctToppings: Set[Toppings] = {
            Toppings.GUACAMOLE, Toppings.SOY_SAUCE, 
            Toppings.HOT_SAUCE, Toppings.CRISPY_STRIPS, topping}
        assert entree.toppings == correctToppings

    @pytest.mark.parametrize("topping", [Toppings.SOUR_CREAM, Toppings.ONIONS, Toppings.FRESH_HERBS])
    def test_removing_toppings_removes_from_topping_list(self, topping):
        entree = YahtzeePoke()
        entree.add_topping(topping)
        entree.remove_topping(topping)
        correctToppings: Set[Toppings] = {
            Toppings.GUACAMOLE, Toppings.SOY_SAUCE, 
            Toppings.HOT_SAUCE, Toppings.CRISPY_STRIPS}
        assert entree.toppings == correctToppings

    def test_two_instances_of_same_object_are_equal(self):
        entree1 = YahtzeePoke()
        entree2 = YahtzeePoke()
        assert entree1 == entree2

    def test_two_instances_with_different_bases(self):
        entree1 = YahtzeePoke()
        entree2 = YahtzeePoke()
        entree2.base = Base.CHIPS
        assert not entree1 == entree2
    
    def test_two_instances_with_different_ingredients(self):
        entree1 = YahtzeePoke()
        entree2 = YahtzeePoke()
        entree2.veggies = False
        assert not entree1 == entree2
    
    def test_two_instances_with_different_toppings(self):
        entree1 = YahtzeePoke()
        entree2 = YahtzeePoke()
        entree2.add_topping(Toppings.SOUR_CREAM)
        assert not entree1 == entree2

    def test_two_different_objects(self):
        entree1 = YahtzeePoke()
        entree2 = ClueChili()
        assert not entree1 == entree2
