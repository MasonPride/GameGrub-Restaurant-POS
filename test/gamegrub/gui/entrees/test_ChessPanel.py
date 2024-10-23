"""Test file for ChessPanel.

Author: Mason Pride
Version: 0.1
"""
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from src.gamegrub.data.entrees.Chess import ChessChickenParm
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings
from src.gamegrub.gui.PrimaryWindow import PrimaryWindow
from src.gamegrub.gui.entrees.ChessPanel import ChessPanel
import pytest


class TestChessPanel:
    """Test Class for ChessPanel."""

    def test_default_constructor(self) -> None:
        """Test the default constructor."""
        panel: ChessPanel = ChessPanel(PrimaryWindow())
        assert_that(panel._item, is_(ChessChickenParm()))

    def test_bad_action_command(self) -> None:
        """Test a bad action performed."""
        panel: ChessPanel = ChessPanel(PrimaryWindow())
        try:
            panel.action_performed("bad")
        except Exception:
            pytest.fail("Unexpected Exception")

    @pytest.mark.parametrize("base", Base)
    def test_base_combo_box(self, base: Base) -> None:
        """Test all bases combo box."""
        item: ChessChickenParm = ChessChickenParm()
        panel: ChessPanel = ChessPanel(PrimaryWindow(), item)
        panel._base.set(str(base))
        panel.action_performed("save")
        assert_that(item.base, is_(base))

    @pytest.mark.parametrize("base", Base)
    def test_base_combo_box_set_correctly(self, base: Base) -> None:
        """Test all bases combo box is correct."""
        item: ChessChickenParm = ChessChickenParm()
        item.base = base
        panel: ChessPanel = ChessPanel(PrimaryWindow(), item)
        assert_that(panel._base.get(), is_(str(base)))

    def test_red_sauce_check_button(self) -> None:
        """Test red sauce check button."""
        item: ChessChickenParm = ChessChickenParm()
        panel: ChessPanel = ChessPanel(PrimaryWindow(), item)
        panel._red_sauce.set(False)
        panel.action_performed("save")
        assert_that(item.red_sauce, is_(False))
        panel._red_sauce.set(True)
        panel.action_performed("save")
        assert_that(item.red_sauce, is_(True))

    def test_red_sauce_check_button_set_correctly(self) -> None:
        """Test red sauce set correctly."""
        item: ChessChickenParm = ChessChickenParm()
        item.red_sauce = False
        panel: ChessPanel = ChessPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._red_sauce.get(), is_(False))
        item.red_sauce = True
        panel: ChessPanel = ChessPanel(PrimaryWindow(), item)
        assert_that(panel._red_sauce.get(), is_(True))

    def test_crispy_chicken_check_button(self) -> None:
        """Test red sauce check button."""
        item: ChessChickenParm = ChessChickenParm()
        panel: ChessPanel = ChessPanel(PrimaryWindow(), item)
        panel._crispy_chicken.set(False)
        panel.action_performed("save")
        assert_that(item.crispy_chicken, is_(False))
        panel._crispy_chicken.set(True)
        panel.action_performed("save")
        assert_that(item.crispy_chicken, is_(True))

    def test_crispy_chicken_check_button_set_correctly(self) -> None:
        """Test red sauce set correctly."""
        item: ChessChickenParm = ChessChickenParm()
        item.crispy_chicken = False
        panel: ChessPanel = ChessPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._crispy_chicken.get(), is_(False))
        item.crispy_chicken = True
        panel: ChessPanel = ChessPanel(PrimaryWindow(), item)
        assert_that(panel._crispy_chicken.get(), is_(True))

    @pytest.mark.parametrize("t", Toppings)
    def test_topping_check_button(self, t: Toppings) -> None:
        """Test topping check button."""
        item: ChessChickenParm = ChessChickenParm()
        panel: ChessPanel = ChessPanel(PrimaryWindow(), item)
        panel._toppings[t].set(False)
        panel.action_performed("save")
        assert_that(t in item.toppings, is_(False))
        panel._toppings[t].set(True)
        panel.action_performed("save")
        assert_that(t in item.toppings, is_(True))

    @pytest.mark.parametrize("t", Toppings)
    def test_topping_check_button_set_correctly(self, t: Toppings) -> None:
        """Test check button set correctly."""
        item: ChessChickenParm = ChessChickenParm()
        item.add_topping(t)
        panel: ChessPanel = ChessPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._toppings[t].get(), is_(True))
        item.remove_topping(t)
        panel: ChessPanel = ChessPanel(PrimaryWindow(), item)
        assert_that(panel._toppings[t].get(), is_(False))

    def test_cancel_button(self) -> None:
        """Test the cancel button."""
        item: ChessChickenParm = ChessChickenParm()
        panel: ChessPanel = ChessPanel(PrimaryWindow(), item)
        if item.base == Base.SPAGHETTI:
            panel._base.set(str(Base.RICE))
        else:
            panel._base.set(str(Base.SPAGHETTI))
        panel._red_sauce.set(False)
        panel._crispy_chicken.set(False)
        for t in Toppings:
            panel._toppings[t].set(t not in item.toppings)
        panel.action_performed("cancel")
        unchanged: ChessChickenParm = ChessChickenParm()
        assert_that(item, is_(unchanged))
