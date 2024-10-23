"""Test file for SorryPanel.

Author: Mason Pride
Version: 0.1
"""
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from src.gamegrub.data.drinks.Sorry import SorrySoda
from src.gamegrub.data.enums.Size import Size
from src.gamegrub.gui.PrimaryWindow import PrimaryWindow
from src.gamegrub.gui.drinks.SorryPanel import SorryPanel
import pytest


class TestSorryPanel:
    """Test Class for SorryPanel."""

    def test_default_constructor(self) -> None:
        """Test the default constructor."""
        panel: SorryPanel = SorryPanel(PrimaryWindow())
        assert_that(panel._item, is_(SorrySoda()))

    def test_bad_action_command(self) -> None:
        """Test a bad action performed."""
        panel: SorryPanel = SorryPanel(PrimaryWindow())
        try:
            panel.action_performed("bad")
        except Exception:
            pytest.fail("Unexpected Exception")

    @pytest.mark.parametrize("size", Size)
    def test_size_combo_box(self, size: Size) -> None:
        """Test all bases combo box."""
        item: SorrySoda = SorrySoda()
        panel: SorryPanel = SorryPanel(PrimaryWindow(), item)
        panel._size.set(str(size))
        panel.action_performed("save")
        assert_that(item.size, is_(size))

    def test_cola_check_button(self) -> None:
        """Test cola check button."""
        item: SorrySoda = SorrySoda()
        panel: SorryPanel = SorryPanel(PrimaryWindow(), item)
        panel._cola.set(False)
        panel.action_performed("save")
        assert_that(item.cola, is_(False))
        panel._cola.set(True)
        panel.action_performed("save")
        assert_that(item.cola, is_(True))

    def test_cola_check_button_set_correctly(self) -> None:
        """Test cola set correctly."""
        item: SorrySoda = SorrySoda()
        item.cola = False
        panel: SorryPanel = SorryPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._cola.get(), is_(False))
        item.cola = True
        panel: SorryPanel = SorryPanel(PrimaryWindow(), item)
        assert_that(panel._cola.get(), is_(True))

    def test_cherry_check_button(self) -> None:
        """Test cherry check button."""
        item: SorrySoda = SorrySoda()
        panel: SorryPanel = SorryPanel(PrimaryWindow(), item)
        panel._cherry.set(False)
        panel.action_performed("save")
        assert_that(item.cherry, is_(False))
        panel._cherry.set(True)
        panel.action_performed("save")
        assert_that(item.cherry, is_(True))

    def test_cherry_check_button_set_correctly(self) -> None:
        """Test cherry set correctly."""
        item: SorrySoda = SorrySoda()
        item.cherry = False
        panel: SorryPanel = SorryPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._cherry.get(), is_(False))
        item.cherry = True
        panel: SorryPanel = SorryPanel(PrimaryWindow(), item)
        assert_that(panel._cherry.get(), is_(True))

    def test_grape_check_button(self) -> None:
        """Test grape check button."""
        item: SorrySoda = SorrySoda()
        panel: SorryPanel = SorryPanel(PrimaryWindow(), item)
        panel._grape.set(False)
        panel.action_performed("save")
        assert_that(item.grape, is_(False))
        panel._grape.set(True)
        panel.action_performed("save")
        assert_that(item.grape, is_(True))

    def test_grape_check_button_set_correctly(self) -> None:
        """Test grape set correctly."""
        item: SorrySoda = SorrySoda()
        item.grape = False
        panel: SorryPanel = SorryPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._grape.get(), is_(False))
        item.grape = True
        panel: SorryPanel = SorryPanel(PrimaryWindow(), item)
        assert_that(panel._grape.get(), is_(True))

    def test_orange_check_button(self) -> None:
        """Test orange check button."""
        item: SorrySoda = SorrySoda()
        panel: SorryPanel = SorryPanel(PrimaryWindow(), item)
        panel._orange.set(False)
        panel.action_performed("save")
        assert_that(item.orange, is_(False))
        panel._orange.set(True)
        panel.action_performed("save")
        assert_that(item.orange, is_(True))

    def test_orange_check_button_set_correctly(self) -> None:
        """Test orange set correctly."""
        item: SorrySoda = SorrySoda()
        item.orange = False
        panel: SorryPanel = SorryPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._orange.get(), is_(False))
        item.orange = True
        panel: SorryPanel = SorryPanel(PrimaryWindow(), item)
        assert_that(panel._orange.get(), is_(True))

    def test_cancel_button(self) -> None:
        """Test the cancel button."""
        item: SorrySoda = SorrySoda()
        panel: SorryPanel = SorryPanel(PrimaryWindow(), item)
        panel._cola.set(False)
        panel._cherry.set(False)
        panel._grape.set(False)
        panel.action_performed("cancel")
        unchanged: SorrySoda = SorrySoda()
        assert_that(item, is_(unchanged))
