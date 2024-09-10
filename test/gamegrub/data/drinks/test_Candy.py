"""Test Class for CandyLandShake.

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


class TestCandy():
    """Test class for 'srs.gamegrub.data.drinks.Candy.py'."""

    def test_size_default_is_junior(self):
        drink = CandyLandShake()
        assert drink.size == Size.JUNIOR

    def test_instructions_list_should_be_empty_on_init(self):
        drink = CandyLandShake()
        assert not drink.instructions

    def test_junior_price_is_correct(self):
        drink = CandyLandShake()
        drink.size = Size.JUNIOR
        assert drink.price == 5.75

    def test_classic_price_is_correct(self):
        drink = CandyLandShake()
        drink.size = Size.CLASSIC
        assert drink.price == 7.45

    def test_winner_price_is_correct(self):
        drink = CandyLandShake()
        drink.size = Size.WINNER
        assert drink.price == 9.55
    
    def test_junior_calories_is_correct(self):
        drink = CandyLandShake()
        drink.size = Size.JUNIOR
        assert drink.calories == 770

    def test_classic_calories_is_correct(self):
        drink = CandyLandShake()
        drink.size = Size.CLASSIC
        assert drink.calories == 1215

    def test_winner_calories_is_correct(self):
        drink = CandyLandShake()
        drink.size = Size.WINNER
        assert drink.calories == 1465

    def test_junior_string_is_correct(self, capsys):
        drink = CandyLandShake()
        print(drink)
        captured = capsys.readouterr()
        assert captured.out == "Junior Candy Land Shake\n", "Unexpected Output"

    def test_classic_string_is_correct(self, capsys):
        drink = CandyLandShake()
        drink.size = Size.CLASSIC
        print(drink)
        captured = capsys.readouterr()
        assert captured.out == "Classic Candy Land Shake\n", "Unexpected Output"

    def test_winner_string_is_correct(self, capsys):
        drink = CandyLandShake()
        drink.size = Size.WINNER
        print(drink)
        captured = capsys.readouterr()
        assert captured.out == "Winner Candy Land Shake\n", "Unexpected Output"

    def test_default_flavors_is_correct(self):
        drink = CandyLandShake()
        assert drink.chocolate == True and drink.vanilla == False and drink.strawberry == False

    def test_default_flavors_instructions_is_zero(self):
        drink = CandyLandShake()
        assert len(drink.instructions) == 0

    def test_remove_default_flavor_instructions_is_one(self):
        drink = CandyLandShake()
        drink.chocolate = False
        assert len(drink.instructions) == 1

    def test_add_vanilla_flavor(self):
        drink = CandyLandShake()
        drink.vanilla = True
        assert drink.chocolate == True and drink.vanilla == True and drink.strawberry == False

    def test_add_vanilla_flavor_instructions_is_one(self):
        drink = CandyLandShake()
        drink.vanilla = True
        assert len(drink.instructions) == 1

    def test_remove_vanilla_flavor_instructions_is_zero(self):
        drink = CandyLandShake()
        drink.vanilla = True
        drink.vanilla = False
        assert len(drink.instructions) == 0

    def test_add_strawberry_flavor(self):
        drink = CandyLandShake()
        drink.strawberry = True
        assert drink.chocolate == True and drink.vanilla == False and drink.strawberry == True

    def test_add_strawberry_flavor_instructions_is_one(self):
        drink = CandyLandShake()
        drink.strawberry= True
        assert len(drink.instructions) == 1

    def test_remove_strawberry_flavor_instructions_is_zero(self):
        drink = CandyLandShake()
        drink.strawberry = True
        drink.strawberry = False
        assert len(drink.instructions) == 0

    def test_two_instances_of_same_object_are_equal(self):
        drink1 = CandyLandShake()
        drink2 = CandyLandShake()
        assert drink1 == drink2

    def test_two_instances_different_size_not_equal(self):
        drink1 = CandyLandShake()
        drink2 = CandyLandShake()
        drink2.size = Size.CLASSIC
        assert not drink1 == drink2

    def test_two_instances_different_flavors_not_equal(self):
        drink1 = CandyLandShake()
        drink2 = CandyLandShake()
        drink2.vanilla = True
        assert not drink1 == drink2

    def test_two_different_objects_not_equal(self):
        drink = CandyLandShake()
        notDrink = CraniumCoffee()
        assert not drink == notDrink

    def test_add_all_possible_instructions(self):
        drink = CandyLandShake()
        drink.chocolate = False
        drink.vanilla = True
        drink.strawberry = True
        assert len(drink.instructions) == 3
