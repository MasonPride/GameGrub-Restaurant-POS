"""Test file for YahtzeePanel.

Author: Mason Pride
Version: 0.1
"""
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from src.gamegrub.data.entrees.Yahtzee import YahtzeePoke
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings
from src.gamegrub.gui.PrimaryWindow import PrimaryWindow
from src.gamegrub.gui.entrees.YahtzeePanel import YahtzeePanel
import pytest


class TestYahtzeePanel:
    """Test Class for YahtzeePanel."""

    def test_default_constructor(self) -> None:
        """Test the default constructor."""
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow())
        assert_that(panel._item, is_(YahtzeePoke()))

    def test_bad_action_command(self) -> None:
        """Test a bad action performed."""
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow())
        try:
            panel.action_performed("bad")
        except Exception:
            pytest.fail("Unexpected Exception")

    @pytest.mark.parametrize("base", Base)
    def test_base_combo_box(self, base: Base) -> None:
        """Test all bases combo box."""
        item: YahtzeePoke = YahtzeePoke()
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow(), item)
        panel._base.set(str(base))
        panel.action_performed("save")
        assert_that(item.base, is_(base))

    @pytest.mark.parametrize("base", Base)
    def test_base_combo_box_set_correctly(self, base: Base) -> None:
        """Test all bases combo box is correct."""
        item: YahtzeePoke = YahtzeePoke()
        item.base = base
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow(), item)
        assert_that(panel._base.get(), is_(str(base)))

    def test_tuna_check_button(self) -> None:
        """Test tuna check button."""
        item: YahtzeePoke = YahtzeePoke()
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow(), item)
        panel._tuna.set(False)
        panel.action_performed("save")
        assert_that(item.tuna, is_(False))
        panel._tuna.set(True)
        panel.action_performed("save")
        assert_that(item.tuna, is_(True))

    def test_tuna_check_button_set_correctly(self) -> None:
        """Test tuna set correctly."""
        item: YahtzeePoke = YahtzeePoke()
        item.tuna = False
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._tuna.get(), is_(False))
        item.tuna = True
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow(), item)
        assert_that(panel._tuna.get(), is_(True))

    def test_seaweed_check_button(self) -> None:
        """Test seaweed check button."""
        item: YahtzeePoke = YahtzeePoke()
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow(), item)
        panel._seaweed.set(False)
        panel.action_performed("save")
        assert_that(item.seaweed, is_(False))
        panel._seaweed.set(True)
        panel.action_performed("save")
        assert_that(item.seaweed, is_(True))

    def test_seaweed_check_button_set_correctly(self) -> None:
        """Test spicy beef set correctly."""
        item: YahtzeePoke = YahtzeePoke()
        item.seaweed = False
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._seaweed.get(), is_(False))
        item.seaweed = True
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow(), item)
        assert_that(panel._seaweed.get(), is_(True))

    def test_veggies_check_button(self) -> None:
        """Test veggies check button."""
        item: YahtzeePoke = YahtzeePoke()
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow(), item)
        panel._veggies.set(False)
        panel.action_performed("save")
        assert_that(item.veggies, is_(False))
        panel._veggies.set(True)
        panel.action_performed("save")
        assert_that(item.veggies, is_(True))

    def test_veggies_check_button_set_correctly(self) -> None:
        """Test veggies set correctly."""
        item: YahtzeePoke = YahtzeePoke()
        item.veggies = False
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._veggies.get(), is_(False))
        item.veggies = True
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow(), item)
        assert_that(panel._veggies.get(), is_(True))

    @pytest.mark.parametrize("t", Toppings)
    def test_topping_check_button(self, t: Toppings) -> None:
        """Test topping check button."""
        item: YahtzeePoke = YahtzeePoke()
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow(), item)
        panel._toppings[t].set(False)
        panel.action_performed("save")
        assert_that(t in item.toppings, is_(False))
        panel._toppings[t].set(True)
        panel.action_performed("save")
        assert_that(t in item.toppings, is_(True))

    @pytest.mark.parametrize("t", Toppings)
    def test_topping_check_button_set_correctly(self, t: Toppings) -> None:
        """Test check button set correctly."""
        item: YahtzeePoke = YahtzeePoke()
        item.add_topping(t)
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._toppings[t].get(), is_(True))
        item.remove_topping(t)
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow(), item)
        assert_that(panel._toppings[t].get(), is_(False))

    def test_cancel_button(self) -> None:
        """Test the cancel button."""
        item: YahtzeePoke = YahtzeePoke()
        panel: YahtzeePanel = YahtzeePanel(PrimaryWindow(), item)
        if item.base == Base.SPAGHETTI:
            panel._base.set(str(Base.RICE))
        else:
            panel._base.set(str(Base.SPAGHETTI))
        panel._tuna.set(False)
        panel._seaweed.set(False)
        panel._veggies.set(False)
        for t in Toppings:
            panel._toppings[t].set(t not in item.toppings)
        panel.action_performed("cancel")
        unchanged: YahtzeePoke = YahtzeePoke()
        assert_that(item, is_(unchanged))
