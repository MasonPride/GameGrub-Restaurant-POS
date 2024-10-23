"""Test file for CraniumPanel.

Author: Mason Pride
Version: 0.1
"""
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from src.gamegrub.data.drinks.Cranium import CraniumCoffee
from src.gamegrub.data.enums.Size import Size
from src.gamegrub.gui.PrimaryWindow import PrimaryWindow
from src.gamegrub.gui.drinks.CraniumPanel import CraniumPanel
import pytest


class TestCraniumPanel:
    """Test Class for CraniumPanel."""

    def test_default_constructor(self) -> None:
        """Test the default constructor."""
        panel: CraniumPanel = CraniumPanel(PrimaryWindow())
        assert_that(panel._item, is_(CraniumCoffee()))

    def test_bad_action_command(self) -> None:
        """Test a bad action performed."""
        panel: CraniumPanel = CraniumPanel(PrimaryWindow())
        try:
            panel.action_performed("bad")
        except Exception:
            pytest.fail("Unexpected Exception")

    @pytest.mark.parametrize("size", Size)
    def test_size_combo_box(self, size: Size) -> None:
        """Test all bases combo box."""
        item: CraniumCoffee = CraniumCoffee()
        panel: CraniumPanel = CraniumPanel(PrimaryWindow(), item)
        panel._size.set(str(size))
        panel.action_performed("save")
        assert_that(item.size, is_(size))

    def test_milk_check_button(self) -> None:
        """Test milk check button."""
        item: CraniumCoffee = CraniumCoffee()
        panel: CraniumPanel = CraniumPanel(PrimaryWindow(), item)
        panel._milk.set(False)
        panel.action_performed("save")
        assert_that(item.milk, is_(False))
        panel._milk.set(True)
        panel.action_performed("save")
        assert_that(item.milk, is_(True))

    def test_milk_check_button_set_correctly(self) -> None:
        """Test milk set correctly."""
        item: CraniumCoffee = CraniumCoffee()
        item.milk = False
        panel: CraniumPanel = CraniumPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._milk.get(), is_(False))
        item.milk = True
        panel: CraniumPanel = CraniumPanel(PrimaryWindow(), item)
        assert_that(panel._milk.get(), is_(True))

    def test_chocolate_check_button(self) -> None:
        """Test chocolate check button."""
        item: CraniumCoffee = CraniumCoffee()
        panel: CraniumPanel = CraniumPanel(PrimaryWindow(), item)
        panel._chocolate.set(False)
        panel.action_performed("save")
        assert_that(item.chocolate, is_(False))
        panel._chocolate.set(True)
        panel.action_performed("save")
        assert_that(item.chocolate, is_(True))

    def test_chocolate_check_button_set_correctly(self) -> None:
        """Test chocolate set correctly."""
        item: CraniumCoffee = CraniumCoffee()
        item.chocolate = False
        panel: CraniumPanel = CraniumPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._chocolate.get(), is_(False))
        item.chocolate = True
        panel: CraniumPanel = CraniumPanel(PrimaryWindow(), item)
        assert_that(panel._chocolate.get(), is_(True))

    def test_caramel_check_button(self) -> None:
        """Test caramel check button."""
        item: CraniumCoffee = CraniumCoffee()
        panel: CraniumPanel = CraniumPanel(PrimaryWindow(), item)
        panel._caramel.set(False)
        panel.action_performed("save")
        assert_that(item.caramel, is_(False))
        panel._caramel.set(True)
        panel.action_performed("save")
        assert_that(item.caramel, is_(True))

    def test_caramel_check_button_set_correctly(self) -> None:
        """Test caramel set correctly."""
        item: CraniumCoffee = CraniumCoffee()
        item.caramel = False
        panel: CraniumPanel = CraniumPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._caramel.get(), is_(False))
        item.caramel = True
        panel: CraniumPanel = CraniumPanel(PrimaryWindow(), item)
        assert_that(panel._caramel.get(), is_(True))

    def test_mint_check_button(self) -> None:
        """Test mint check button."""
        item: CraniumCoffee = CraniumCoffee()
        panel: CraniumPanel = CraniumPanel(PrimaryWindow(), item)
        panel._mint.set(False)
        panel.action_performed("save")
        assert_that(item.mint, is_(False))
        panel._mint.set(True)
        panel.action_performed("save")
        assert_that(item.mint, is_(True))

    def test_mint_check_button_set_correctly(self) -> None:
        """Test mint set correctly."""
        item: CraniumCoffee = CraniumCoffee()
        item.mint = False
        panel: CraniumPanel = CraniumPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._mint.get(), is_(False))
        item.mint = True
        panel: CraniumPanel = CraniumPanel(PrimaryWindow(), item)
        assert_that(panel._mint.get(), is_(True))

    def test_cancel_button(self) -> None:
        """Test the cancel button."""
        item: CraniumCoffee = CraniumCoffee()
        panel: CraniumPanel = CraniumPanel(PrimaryWindow(), item)
        panel._milk.set(False)
        panel._chocolate.set(False)
        panel._caramel.set(False)
        panel.action_performed("cancel")
        unchanged: CraniumCoffee = CraniumCoffee()
        assert_that(item, is_(unchanged))
