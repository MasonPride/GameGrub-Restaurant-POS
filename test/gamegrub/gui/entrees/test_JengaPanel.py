"""Test file for JengaPanel.

Author: Mason Pride
Version: 0.1
"""
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from src.gamegrub.data.entrees.Jenga import JengaNachos
from src.gamegrub.data.enums.Base import Base
from src.gamegrub.data.enums.Toppings import Toppings
from src.gamegrub.gui.PrimaryWindow import PrimaryWindow
from src.gamegrub.gui.entrees.JengaPanel import JengaPanel
import pytest


class TestJengaPanel:
    """Test Class for JengaPanel."""

    def test_default_constructor(self) -> None:
        """Test the default constructor."""
        panel: JengaPanel = JengaPanel(PrimaryWindow())
        assert_that(panel._item, is_(JengaNachos()))

    def test_bad_action_command(self) -> None:
        """Test a bad action performed."""
        panel: JengaPanel = JengaPanel(PrimaryWindow())
        try:
            panel.action_performed("bad")
        except Exception:
            pytest.fail("Unexpected Exception")

    @pytest.mark.parametrize("base", Base)
    def test_base_combo_box(self, base: Base) -> None:
        """Test all bases combo box."""
        item: JengaNachos = JengaNachos()
        panel: JengaPanel = JengaPanel(PrimaryWindow(), item)
        panel._base.set(str(base))
        panel.action_performed("save")
        assert_that(item.base, is_(base))

    @pytest.mark.parametrize("base", Base)
    def test_base_combo_box_set_correctly(self, base: Base) -> None:
        """Test all bases combo box is correct."""
        item: JengaNachos = JengaNachos()
        item.base = base
        panel: JengaPanel = JengaPanel(PrimaryWindow(), item)
        assert_that(panel._base.get(), is_(str(base)))

    def test_spicy_beef_check_button(self) -> None:
        """Test spicy beef check button."""
        item: JengaNachos = JengaNachos()
        panel: JengaPanel = JengaPanel(PrimaryWindow(), item)
        panel._spicy_beef.set(False)
        panel.action_performed("save")
        assert_that(item.spicy_beef, is_(False))
        panel._spicy_beef.set(True)
        panel.action_performed("save")
        assert_that(item.spicy_beef, is_(True))

    def test_spicy_beef_check_button_set_correctly(self) -> None:
        """Test spicy beef set correctly."""
        item: JengaNachos = JengaNachos()
        item.spicy_beef = False
        panel: JengaPanel = JengaPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._spicy_beef.get(), is_(False))
        item.spicy_beef = True
        panel: JengaPanel = JengaPanel(PrimaryWindow(), item)
        assert_that(panel._spicy_beef.get(), is_(True))

    def test_beans_check_button(self) -> None:
        """Test beans check button."""
        item: JengaNachos = JengaNachos()
        panel: JengaPanel = JengaPanel(PrimaryWindow(), item)
        panel._beans.set(False)
        panel.action_performed("save")
        assert_that(item.beans, is_(False))
        panel._beans.set(True)
        panel.action_performed("save")
        assert_that(item.beans, is_(True))

    def test_beans_check_button_set_correctly(self) -> None:
        """Test beans set correctly."""
        item: JengaNachos = JengaNachos()
        item.beans = False
        panel: JengaPanel = JengaPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._beans.get(), is_(False))
        item.beans = True
        panel: JengaPanel = JengaPanel(PrimaryWindow(), item)
        assert_that(panel._beans.get(), is_(True))

    @pytest.mark.parametrize("t", Toppings)
    def test_topping_check_button(self, t: Toppings) -> None:
        """Test topping check button."""
        item: JengaNachos = JengaNachos()
        panel: JengaPanel = JengaPanel(PrimaryWindow(), item)
        panel._toppings[t].set(False)
        panel.action_performed("save")
        assert_that(t in item.toppings, is_(False))
        panel._toppings[t].set(True)
        panel.action_performed("save")
        assert_that(t in item.toppings, is_(True))

    @pytest.mark.parametrize("t", Toppings)
    def test_topping_check_button_set_correctly(self, t: Toppings) -> None:
        """Test check button set correctly."""
        item: JengaNachos = JengaNachos()
        item.add_topping(t)
        panel: JengaPanel = JengaPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._toppings[t].get(), is_(True))
        item.remove_topping(t)
        panel: JengaPanel = JengaPanel(PrimaryWindow(), item)
        assert_that(panel._toppings[t].get(), is_(False))

    def test_cancel_button(self) -> None:
        """Test the cancel button."""
        item: JengaNachos = JengaNachos()
        panel: JengaPanel = JengaPanel(PrimaryWindow(), item)
        if item.base == Base.SPAGHETTI:
            panel._base.set(str(Base.RICE))
        else:
            panel._base.set(str(Base.SPAGHETTI))
        panel._spicy_beef.set(False)
        panel._beans.set(False)
        for t in Toppings:
            panel._toppings[t].set(t not in item.toppings)
        panel.action_performed("cancel")
        unchanged: JengaNachos = JengaNachos()
        assert_that(item, is_(unchanged))
