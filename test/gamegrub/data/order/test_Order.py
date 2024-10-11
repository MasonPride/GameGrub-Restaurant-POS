"""Test Class for Order.py.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
import pytest
from src.gamegrub.data.order.Order import Order
from unittest.mock import patch, PropertyMock, Mock
from src.gamegrub.data.entrees.Clue import ClueChili
from src.gamegrub.data.sides.Risk import RiskBites
from src.gamegrub.data.drinks.Candy import CandyLandShake


class TestOrder():
    """Test class for 'srs.gamegrub.data.order.Order.py."""

    def test_new_order_has_zero_items(self):
        order = Order()
        assert len(order) == 0

    def test_new_order_subtotal_is_zero(self):
        order = Order()
        assert order.subtotal == 0.0

    def test_new_order_tax_is_zero(self):
        order = Order()
        assert order.tax == 0

    def test_new_order_total_is_zero(self):
        order = Order()
        assert order.total == 0.0
    
    def test_new_order_calories_is_zero(self):
        order = Order()
        assert order.calories == 0
    """
    def test_set_tax_rate_below_zero(self):
        order = Order()
        with pytest.raises(Exception) as info:
    """
    @patch('src.gamegrub.data.entrees.Clue', spec=ClueChili)
    @patch('src.gamegrub.data.sides.Risk', spec=RiskBites)
    @patch('src.gamegrub.data.drinks.Candy', spec=CandyLandShake)
    def test_size_of_order_increases_on_add(self, mock_drink, mock_side, mock_entree):
        order = Order()
        order.add_item(mock_entree)
        assert len(order) == 1
        order.add_item(mock_side)
        assert len(order) == 2
        order.add_item(mock_drink)
        assert len(order) == 3

    @patch('src.gamegrub.data.entrees.Clue', spec=ClueChili)
    @patch('src.gamegrub.data.sides.Risk', spec=RiskBites)
    @patch('src.gamegrub.data.drinks.Candy', spec=CandyLandShake)
    def test_size_of_order_decreases_on_remove(self, mock_drink, mock_side, mock_entree):
        order = Order()
        order.add_item(mock_entree)
        order.add_item(mock_side)
        order.add_item(mock_drink)
        assert len(order) == 3
        order.remove_item(mock_entree)
        assert len(order) == 2
        order.remove_item(mock_side)
        assert len(order) == 1
        order.remove_item(mock_drink)
        assert len(order) == 0

    """
    @patch('src.gamegrub.data.entrees.Clue', spec=ClueChili)
    @patch('src.gamegrub.data.sides.Risk', spec=RiskBites)
    @patch('src.gamegrub.data.drinks.Candy', spec=CandyLandShake)
    def test_size_of_order_subtotal_increases_on_add(self, mock_drink, mock_side, mock_entree):
        order = Order()
        order.add_item(mock_entree)
        assert order.subtotal == 10.45
    """

