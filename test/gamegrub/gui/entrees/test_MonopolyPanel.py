"""Test file for MonopolyPanel.

Author: Mason Pride
Version: 0.1
"""
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from src.gamegrub.data.entrees.Monopoly import MonopolyBowl
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings
from src.gamegrub.gui.PrimaryWindow import PrimaryWindow
from src.gamegrub.gui.entrees.MonopolyPanel import MonopolyPanel
import pytest


class TestMonopolyPanel:
    """Test Class for MonopolyPanel."""

    def test_default_constructor(self) -> None:
        """Test the default constructor."""
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow())
        assert_that(panel._item, is_(MonopolyBowl()))

    def test_bad_action_command(self) -> None:
        """Test a bad action performed."""
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow())
        try:
            panel.action_performed("bad")
        except Exception:
            pytest.fail("Unexpected Exception")

    @pytest.mark.parametrize("base", Base)
    def test_base_combo_box(self, base: Base) -> None:
        """Test all bases combo box."""
        item: MonopolyBowl = MonopolyBowl()
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        panel._base.set(str(base))
        panel.action_performed("save")
        assert_that(item.base, is_(base))

    @pytest.mark.parametrize("base", Base)
    def test_base_combo_box_set_correctly(self, base: Base) -> None:
        """Test all bases combo box is correct."""
        item: MonopolyBowl = MonopolyBowl()
        item.base = base
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        assert_that(panel._base.get(), is_(str(base)))

    def test_crispy_chicken_check_button(self) -> None:
        """Test crispy_chicken check button."""
        item: MonopolyBowl = MonopolyBowl()
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        panel._crispy_chicken.set(False)
        panel.action_performed("save")
        assert_that(item.crispy_chicken, is_(False))
        panel._crispy_chicken.set(True)
        panel.action_performed("save")
        assert_that(item.crispy_chicken, is_(True))

    def test_crispy_chicken_check_button_set_correctly(self) -> None:
        """Test crispy chicken set correctly."""
        item: MonopolyBowl = MonopolyBowl()
        item.crispy_chicken = False
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._crispy_chicken.get(), is_(False))
        item.crispy_chicken = True
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        assert_that(panel._crispy_chicken.get(), is_(True))

    def test_spicy_beef_check_button(self) -> None:
        """Test spicy beef check button."""
        item: MonopolyBowl = MonopolyBowl()
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        panel._spicy_beef.set(False)
        panel.action_performed("save")
        assert_that(item.spicy_beef, is_(False))
        panel._spicy_beef.set(True)
        panel.action_performed("save")
        assert_that(item.spicy_beef, is_(True))

    def test_spicy_beef_check_button_set_correctly(self) -> None:
        """Test spicy beef set correctly."""
        item: MonopolyBowl = MonopolyBowl()
        item.spicy_beef = False
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._spicy_beef.get(), is_(False))
        item.spicy_beef = True
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        assert_that(panel._spicy_beef.get(), is_(True))

    def test_veggies_check_button(self) -> None:
        """Test veggies check button."""
        item: MonopolyBowl = MonopolyBowl()
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        panel._veggies.set(False)
        panel.action_performed("save")
        assert_that(item.veggies, is_(False))
        panel._veggies.set(True)
        panel.action_performed("save")
        assert_that(item.veggies, is_(True))

    def test_veggies_check_button_set_correctly(self) -> None:
        """Test veggies set correctly."""
        item: MonopolyBowl = MonopolyBowl()
        item.veggies = False
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._veggies.get(), is_(False))
        item.veggies = True
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        assert_that(panel._veggies.get(), is_(True))

    def test_beans_check_button(self) -> None:
        """Test beans check button."""
        item: MonopolyBowl = MonopolyBowl()
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        panel._beans.set(False)
        panel.action_performed("save")
        assert_that(item.beans, is_(False))
        panel._beans.set(True)
        panel.action_performed("save")
        assert_that(item.beans, is_(True))

    def test_beans_check_button_set_correctly(self) -> None:
        """Test beans set correctly."""
        item: MonopolyBowl = MonopolyBowl()
        item.beans = False
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._beans.get(), is_(False))
        item.beans = True
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        assert_that(panel._beans.get(), is_(True))

    @pytest.mark.parametrize("t", Toppings)
    def test_topping_check_button(self, t: Toppings) -> None:
        """Test topping check button."""
        item: MonopolyBowl = MonopolyBowl()
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        panel._toppings[t].set(False)
        panel.action_performed("save")
        assert_that(t in item.toppings, is_(False))
        panel._toppings[t].set(True)
        panel.action_performed("save")
        assert_that(t in item.toppings, is_(True))

    @pytest.mark.parametrize("t", Toppings)
    def test_topping_check_button_set_correctly(self, t: Toppings) -> None:
        """Test check button set correctly."""
        item: MonopolyBowl = MonopolyBowl()
        item.add_topping(t)
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._toppings[t].get(), is_(True))
        item.remove_topping(t)
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        assert_that(panel._toppings[t].get(), is_(False))

    def test_cancel_button(self) -> None:
        """Test the cancel button."""
        item: MonopolyBowl = MonopolyBowl()
        panel: MonopolyPanel = MonopolyPanel(PrimaryWindow(), item)
        if item.base == Base.SPAGHETTI:
            panel._base.set(str(Base.RICE))
        else:
            panel._base.set(str(Base.SPAGHETTI))
        panel._crispy_chicken.set(False)
        panel._spicy_beef.set(False)
        panel._veggies.set(False)
        panel._beans.set(False)
        for t in Toppings:
            panel._toppings[t].set(t not in item.toppings)
        panel.action_performed("cancel")
        unchanged: MonopolyBowl = MonopolyBowl()
        assert_that(item, is_(unchanged))
