"""Test Class for CraniumCoffee.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.gamegrub.data.drinks.Candy import CandyLandShake
from src.gamegrub.data.drinks.Cranium import CraniumCoffee
from src.gamegrub.data.enums.Size import Size


class TestCranium():
    """Test class for 'srs.gamegrub.data.drinks.Cranium.py'."""

    def test_size_default_is_junior(self):
        drink = CraniumCoffee()
        assert drink.size == Size.JUNIOR

    def test_instructions_list_should_be_empty_on_init(self):
        drink = CraniumCoffee()
        assert not drink.instructions

    def test_junior_price_is_correct(self):
        drink = CraniumCoffee()
        drink.size = Size.JUNIOR
        assert drink.price == 4.35

    def test_classic_price_is_correct(self):
        drink = CraniumCoffee()
        drink.size = Size.CLASSIC
        assert drink.price == 5.25
    
    def test_winner_price_is_correct(self):
        drink = CraniumCoffee()
        drink.size = Size.WINNER
        assert drink.price == 6.00
    
    def test_junior_calories_is_correct(self):
        drink = CraniumCoffee()
        drink.size = Size.JUNIOR
        assert drink.calories == 380

    def test_classic_calories_is_correct(self):
        drink = CraniumCoffee()
        drink.size = Size.CLASSIC
        assert drink.calories == 495

    def test_winner_calories_is_correct(self):
        drink = CraniumCoffee()
        drink.size = Size.WINNER
        assert drink.calories == 585
    
    def test_junior_string_is_correct(self, capsys):
        drink = CraniumCoffee()
        print(drink)
        captured = capsys.readouterr()
        assert captured.out == "Junior Cranium Coffee\n", "Unexpected Output"
    
    def test_classic_string_is_correct(self, capsys):
        drink = CraniumCoffee()
        drink.size = Size.CLASSIC
        print(drink)
        captured = capsys.readouterr()
        assert captured.out == "Classic Cranium Coffee\n", "Unexpected Output"

    def test_winner_string_is_correct(self, capsys):
        drink = CraniumCoffee()
        drink.size = Size.WINNER
        print(drink)
        captured = capsys.readouterr()
        assert captured.out == "Winner Cranium Coffee\n", "Unexpected Output"

    def test_default_flavors_is_correct(self):
        drink = CraniumCoffee()
        assert drink.milk == True and drink.caramel == False and drink.mint == False and drink.chocolate == False

    def test_default_flavors_instructions_is_zero(self):
        drink = CraniumCoffee()
        assert len(drink.instructions) == 0

    def test_remove_default_flavor_instructions_is_one(self):
        drink = CraniumCoffee()
        drink.milk = False
        assert len(drink.instructions) == 1

    def test_add_caramel_flavor(self):
        drink = CraniumCoffee()
        drink.caramel = True
        assert drink.milk == True and drink.chocolate == False and drink.caramel == True and drink.mint == False

    def test_add_caramel_flavor_instructions_is_one(self):
        drink = CraniumCoffee()
        drink.caramel = True
        assert len(drink.instructions) == 1

    def test_remove_caramel_flavor_instructions_is_zero(self):
        drink = CraniumCoffee()
        drink.caramel = True
        drink.caramel = False
        assert len(drink.instructions) == 0

    def test_add_chocolate_flavor(self):
        drink = CraniumCoffee()
        drink.chocolate = True
        assert drink.milk == True and drink.chocolate == True and drink.caramel == False and drink.mint == False

    def test_add_chocolate_flavor_instructions_is_one(self):
        drink = CraniumCoffee()
        drink.chocolate = True
        assert len(drink.instructions) == 1

    def test_remove_chocolate_flavor_instructions_is_zero(self):
        drink = CraniumCoffee()
        drink.chocolate = True
        drink.chocolate = False
        assert len(drink.instructions) == 0
    
    def test_add_mint_flavor(self):
        drink = CraniumCoffee()
        drink.mint = True
        assert drink.milk == True and drink.chocolate == False and drink.caramel == False and drink.mint == True

    def test_add_mint_flavor_instructions_is_one(self):
        drink = CraniumCoffee()
        drink.mint = True
        assert len(drink.instructions) == 1

    def test_remove_mint_flavor_instructions_is_zero(self):
        drink = CraniumCoffee()
        drink.mint = True
        drink.mint = False
        assert len(drink.instructions) == 0

    def test_two_instances_of_same_object_are_equal(self):
        drink1 = CraniumCoffee()
        drink2 = CraniumCoffee()
        assert drink1 == drink2

    def test_two_instances_different_size_not_equal(self):
        drink1 = CraniumCoffee()
        drink2 = CraniumCoffee()
        drink2.size = Size.CLASSIC
        assert not drink1 == drink2

    def test_two_instances_different_flavors_not_equal(self):
        drink1 = CraniumCoffee()
        drink2 = CraniumCoffee()
        drink2.chocolate = True
        assert not drink1 == drink2

    def test_two_different_objects_not_equal(self):
        drink = CraniumCoffee()
        notDrink = CandyLandShake()
        assert not drink == notDrink

    def test_add_all_possible_instructions(self):
        drink = CraniumCoffee()
        drink.milk = False
        drink.caramel = True
        drink.chocolate = True
        drink.mint = True
        assert len(drink.instructions) == 4
