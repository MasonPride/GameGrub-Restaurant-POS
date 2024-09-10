"""Test Class for SorrySoda.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.gamegrub.data.drinks.Sorry import SorrySoda
from src.gamegrub.data.drinks.Cranium import CraniumCoffee
from src.gamegrub.data.enums.Size import Size


class TestSorry():
    """Test class for 'srs.gamegrub.data.drinks.Sorry.py'."""

    def test_size_default_is_junior(self):
        drink = SorrySoda()
        assert drink.size == Size.JUNIOR

    def test_instructions_list_should_be_empty_on_init(self):
        drink = SorrySoda()
        assert not drink.instructions

    def test_junior_price_is_correct(self):
        drink = SorrySoda()
        drink.size = Size.JUNIOR
        assert drink.price == 2.55

    def test_classic_price_is_correct(self):
        drink = SorrySoda()
        drink.size = Size.CLASSIC
        assert drink.price == 3.85

    def test_winner_price_is_correct(self):
        drink = SorrySoda()
        drink.size = Size.WINNER
        assert drink.price == 5.35

    def test_junior_calories_is_correct(self):
        drink = SorrySoda()
        drink.size = Size.JUNIOR
        assert drink.calories == 370

    def test_classic_calories_is_correct(self):
        drink = SorrySoda()
        drink.size = Size.CLASSIC
        assert drink.calories == 535

    def test_winner_calories_is_correct(self):
        drink = SorrySoda()
        drink.size = Size.WINNER
        assert drink.calories == 765
    
    def test_junior_string_is_correct(self, capsys):
        drink = SorrySoda()
        print(drink)
        captured = capsys.readouterr()
        assert captured.out == "Junior Sorry Soda\n", "Unexpected Output"
    
    def test_classic_string_is_correct(self, capsys):
        drink = SorrySoda()
        drink.size = Size.CLASSIC
        print(drink)
        captured = capsys.readouterr()
        assert captured.out == "Classic Sorry Soda\n", "Unexpected Output"

    def test_winner_string_is_correct(self, capsys):
        drink = SorrySoda()
        drink.size = Size.WINNER
        print(drink)
        captured = capsys.readouterr()
        assert captured.out == "Winner Sorry Soda\n", "Unexpected Output"

    def test_default_flavors_is_correct(self):
        drink = SorrySoda()
        assert drink.cola == True and drink.cherry == False and drink.grape == False and drink.orange == False

    def test_default_flavors_instructions_is_zero(self):
        drink = SorrySoda()
        assert len(drink.instructions) == 0

    def test_remove_default_flavor_instructions_is_one(self):
        drink = SorrySoda()
        drink.cola = False
        assert len(drink.instructions) == 1

    def test_add_cherry_flavor(self):
        drink = SorrySoda()
        drink.cherry = True
        assert drink.cola == True and drink.cherry == True and drink.grape == False and drink.orange == False

    def test_add_cherry_flavor_instructions_is_one(self):
        drink = SorrySoda()
        drink.cherry = True
        assert len(drink.instructions) == 1

    def test_remove_cherry_flavor_instructions_is_zero(self):
        drink = SorrySoda()
        drink.cherry = True
        drink.cherry = False
        assert len(drink.instructions) == 0
    
    def test_add_grape_flavor(self):
        drink = SorrySoda()
        drink.grape = True
        assert drink.cola == True and drink.cherry == False and drink.grape == True and drink.orange == False

    def test_add_grape_flavor_instructions_is_one(self):
        drink = SorrySoda()
        drink.grape = True
        assert len(drink.instructions) == 1

    def test_remove_grape_flavor_instructions_is_zero(self):
        drink = SorrySoda()
        drink.grape = True
        drink.grape = False
        assert len(drink.instructions) == 0
    
    def test_add_orange_flavor(self):
        drink = SorrySoda()
        drink.orange = True
        assert drink.cola == True and drink.cherry == False and drink.grape == False and drink.orange == True
    
    def test_add_orange_flavor_instructions_is_one(self):
        drink = SorrySoda()
        drink.orange = True
        assert len(drink.instructions) == 1

    def test_remove_mint_flavor_instructions_is_zero(self):
        drink = SorrySoda()
        drink.orange = True
        drink.orange = False
        assert len(drink.instructions) == 0

    def test_two_instances_of_same_object_are_equal(self):
        drink1 = SorrySoda()
        drink2 = SorrySoda()
        assert drink1 == drink2

    def test_two_instances_different_size_not_equal(self):
        drink1 = SorrySoda()
        drink2 = SorrySoda()
        drink2.size = Size.CLASSIC
        assert not drink1 == drink2

    def test_two_instances_different_flavors_not_equal(self):
        drink1 = SorrySoda()
        drink2 = SorrySoda()
        drink2.orange = True
        assert not drink1 == drink2

    def test_two_different_objects_not_equal(self):
        notDrink = CraniumCoffee()
        drink = SorrySoda()
        assert not drink == notDrink

    def test_add_all_possible_instructions(self):
        drink = SorrySoda()
        drink.cola = False
        drink.cherry = True
        drink.grape = True
        drink.orange = True
        assert len(drink.instructions) == 4
