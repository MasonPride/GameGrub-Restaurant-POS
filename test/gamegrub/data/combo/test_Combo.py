"""Test Class for Combo.py.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.gamegrub.data.combo.Combo import Combo


class TestCombo():

    def test_combo_constructor_takes_string(self):
        combo = Combo("test-combo")
        assert combo.name == "test-combo"

    def test_combo_constructor_takes_no_string(self):
        combo = Combo()
        assert combo.name == None

    def test_combo_constructor_sets_attributes_to_none(self):
        combo = Combo()
        assert combo.entree is None
        assert combo.side is None
        assert combo.drink is None

    def test_combo_price_is_0_on_init(self):
        combo = Combo()
        assert combo.price == 0.0

    def test_combo_calories_is_0_on_init(self):
        combo = Combo()
        assert combo.calories == 0

    def test_discount_can_be_set_to_0(self):
        combo = Combo()
        combo.set_discount(0)
        assert combo.get_discount() == 0