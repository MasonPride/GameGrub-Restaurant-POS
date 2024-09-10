"""Test Class for Monopoly Bowl.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.gamegrub.data.entrees.Monopoly import MonopolyBowl
from src.gamegrub.data.entrees.Clue import ClueChili
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings

class TestMonopoly():
    """Test class for 'srs.gamegrub.data.entrees.Monopoly.py'."""

    def test_instructions_size_is_zero_on_init(self):
        entree = MonopolyBowl()
        assert len(entree.instructions) == 0

    def test_default_base_is_set_correctly(self):
        entree = MonopolyBowl()
        assert entree.base == Base.RICE

    def test_default_toppings_set_correctly(self):
        entree = MonopolyBowl()
        correctToppings: Set[Toppings] = {
            Toppings.ONIONS, Toppings.CHEESE,
            Toppings.GUACAMOLE, Toppings.SOUR_CREAM, 
            Toppings.HOT_SAUCE, Toppings.CRISPY_STRIPS}
        assert entree.toppings == correctToppings

    def test_default_calories_is_correct(self):
        entree = MonopolyBowl()
        assert entree.calories == 1685

    def test_price_of_spaghetti_base(self):
        entree = MonopolyBowl()
        entree.base = Base.SPAGHETTI
        assert entree.price == 19.15

    def test_string_of_spaghetti_base(self, capsys):
        entree = MonopolyBowl()
        entree.base = Base.SPAGHETTI
        print(entree)
        captured = capsys.readouterr()
        assert captured.out == "Monopoly Bowl on Spaghetti\n", "Unexpected Output"

    def test_price_of_rice_base(self):
        entree = MonopolyBowl()
        entree.base = Base.RICE
        assert entree.price == 18.65

    def test_string_of_rice_base(self, capsys):
        entree = MonopolyBowl()
        entree.base = Base.RICE
        print(entree)
        captured = capsys.readouterr()
        assert captured.out == "Monopoly Bowl on Rice\n", "Unexpected Output"

    def test_price_of_chips_base(self):
        entree = MonopolyBowl()
        entree.base = Base.CHIPS
        assert entree.price == 19.65

    def test_string_of_chips_base(self, capsys):
        entree = MonopolyBowl()
        entree.base = Base.CHIPS
        print(entree)
        captured = capsys.readouterr()
        assert captured.out == "Monopoly Bowl on Chips\n", "Unexpected Output"
    
    def test_spicy_beef_true_on_default(self):
        entree = MonopolyBowl()
        assert entree.spicy_beef == True
    
    def test_remove_spicy_beef_adds_to_instructions(self):
        entree = MonopolyBowl()
        entree.spicy_beef = False
        assert len(entree.instructions) == 1

    def test_crispy_chicken_true_on_default(self):
        entree = MonopolyBowl()
        assert entree.crispy_chicken == True

    def test_remove_crispy_chicken_adds_to_instructions(self):
        entree = MonopolyBowl()
        entree.crispy_chicken = False
        assert len(entree.instructions) == 1
    
    def test_beans_true_on_default(self):
        entree = MonopolyBowl()
        assert entree.beans == True
    
    def test_remove_beans_adds_to_instructions(self):
        entree = MonopolyBowl()
        entree.beans = False
        assert len(entree.instructions) == 1

    def test_veggies_true_on_default(self):
        entree = MonopolyBowl()
        assert entree.veggies == True

    def test_remove_veggies_adds_to_instructions(self):
        entree = MonopolyBowl()
        entree.veggies = False
        assert len(entree.instructions) == 1
    
    def test_removing_guacamole_removes_from_toppings(self):
        entree = MonopolyBowl()
        entree.remove_topping(Toppings.GUACAMOLE)
        correctToppings: Set[Toppings] = {
            Toppings.ONIONS, Toppings.CHEESE,
            Toppings.SOUR_CREAM,Toppings.HOT_SAUCE, Toppings.CRISPY_STRIPS}
        assert entree.toppings == correctToppings
    
    def test_removing_cheese_removes_from_toppings(self):
        entree = MonopolyBowl()
        entree.remove_topping(Toppings.CHEESE)
        correctToppings: Set[Toppings] = {
            Toppings.ONIONS,Toppings.GUACAMOLE, Toppings.SOUR_CREAM, 
            Toppings.HOT_SAUCE, Toppings.CRISPY_STRIPS}
        assert entree.toppings == correctToppings
    
    def test_removing_hot_sauce_removes_from_toppings(self):
        entree = MonopolyBowl()
        entree.remove_topping(Toppings.HOT_SAUCE)
        correctToppings: Set[Toppings] = {
            Toppings.ONIONS, Toppings.CHEESE,
            Toppings.GUACAMOLE, Toppings.SOUR_CREAM, 
            Toppings.CRISPY_STRIPS}
        assert entree.toppings == correctToppings

    def test_removing_sour_cream_removes_from_toppings(self):
        entree = MonopolyBowl()
        entree.remove_topping(Toppings.SOUR_CREAM)
        correctToppings: Set[Toppings] = {
            Toppings.ONIONS, Toppings.CHEESE,
            Toppings.GUACAMOLE, Toppings.HOT_SAUCE, 
            Toppings.CRISPY_STRIPS}
        assert entree.toppings == correctToppings

    def test_removing_crispy_strips_removes_from_toppings(self):
        entree = MonopolyBowl()
        entree.remove_topping(Toppings.CRISPY_STRIPS)
        correctToppings: Set[Toppings] = {
            Toppings.ONIONS, Toppings.CHEESE,
            Toppings.GUACAMOLE, Toppings.HOT_SAUCE, 
            Toppings.SOUR_CREAM}
        assert entree.toppings == correctToppings
    
    @pytest.mark.parametrize("topping", [Toppings.SOUR_CREAM, Toppings.ONIONS, Toppings.FRESH_HERBS])
    def test_adding_toppings_to_entree(self, topping):
        entree = MonopolyBowl()
        entree.add_topping(topping)
        correctToppings: Set[Toppings] = {
            Toppings.ONIONS, Toppings.CHEESE,
            Toppings.GUACAMOLE, Toppings.SOUR_CREAM, 
            Toppings.HOT_SAUCE, Toppings.CRISPY_STRIPS, topping}
        assert entree.toppings == correctToppings

    @pytest.mark.parametrize("topping", [Toppings.SOY_SAUCE, Toppings.FRESH_HERBS])
    def test_removing_toppings_removes_from_topping_list(self, topping):
        entree = MonopolyBowl()
        entree.add_topping(topping)
        entree.remove_topping(topping)
        correctToppings: Set[Toppings] = {
            Toppings.ONIONS, Toppings.CHEESE,
            Toppings.GUACAMOLE, Toppings.SOUR_CREAM, 
            Toppings.HOT_SAUCE, Toppings.CRISPY_STRIPS}
        assert entree.toppings == correctToppings

    def test_two_instances_of_same_object_are_equal(self):
        entree1 = MonopolyBowl()
        entree2 = MonopolyBowl()
        assert entree1 == entree2

    def test_two_instances_with_different_bases(self):
        entree1 = MonopolyBowl()
        entree2 = MonopolyBowl()
        entree2.base = Base.CHIPS
        assert not entree1 == entree2
    
    def test_two_instances_with_different_ingredients(self):
        entree1 = MonopolyBowl()
        entree2 = MonopolyBowl()
        entree2.veggies = False
        assert not entree1 == entree2
    
    def test_two_instances_with_different_toppings(self):
        entree1 = MonopolyBowl()
        entree2 = MonopolyBowl()
        entree2.add_topping(Toppings.SOY_SAUCE)
        assert not entree1 == entree2

    def test_two_different_objects(self):
        entree1 = MonopolyBowl()
        entree2 = ClueChili()
        assert not entree1 == entree2
