"""Test file for CandyPanel.

Author: Mason Pride
Version: 0.1
"""
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from src.gamegrub.data.drinks.Candy import CandyLandShake
from src.gamegrub.data.enums.Size import Size
from src.gamegrub.gui.PrimaryWindow import PrimaryWindow
from src.gamegrub.gui.drinks.CandyPanel import CandyPanel
import pytest


class TestCandyPanel:
    """Test Class for CandyPanel."""

    def test_default_constructor(self) -> None:
        """Test the default constructor."""
        panel: CandyPanel = CandyPanel(PrimaryWindow())
        assert_that(panel._item, is_(CandyLandShake()))

    def test_bad_action_command(self) -> None:
        """Test a bad action performed."""
        panel: CandyPanel = CandyPanel(PrimaryWindow())
        try:
            panel.action_performed("bad")
        except Exception:
            pytest.fail("Unexpected Exception")

    @pytest.mark.parametrize("size", Size)
    def test_size_combo_box(self, size: Size) -> None:
        """Test all bases combo box."""
        item: CandyLandShake = CandyLandShake()
        panel: CandyPanel = CandyPanel(PrimaryWindow(), item)
        panel._size.set(str(size))
        panel.action_performed("save")
        assert_that(item.size, is_(size))

    def test_vanilla_check_button(self) -> None:
        """Test vanilla check button."""
        item: CandyLandShake = CandyLandShake()
        panel: CandyPanel = CandyPanel(PrimaryWindow(), item)
        panel._vanilla.set(False)
        panel.action_performed("save")
        assert_that(item.vanilla, is_(False))
        panel._vanilla.set(True)
        panel.action_performed("save")
        assert_that(item.vanilla, is_(True))

    def test_vanilla_check_button_set_correctly(self) -> None:
        """Test vanilla set correctly."""
        item: CandyLandShake = CandyLandShake()
        item.vanilla = False
        panel: CandyPanel = CandyPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._vanilla.get(), is_(False))
        item.vanilla = True
        panel: CandyPanel = CandyPanel(PrimaryWindow(), item)
        assert_that(panel._vanilla.get(), is_(True))

    def test_chocolate_check_button(self) -> None:
        """Test chocolate check button."""
        item: CandyLandShake = CandyLandShake()
        panel: CandyPanel = CandyPanel(PrimaryWindow(), item)
        panel._chocolate.set(False)
        panel.action_performed("save")
        assert_that(item.chocolate, is_(False))
        panel._chocolate.set(True)
        panel.action_performed("save")
        assert_that(item.chocolate, is_(True))

    def test_chocolate_check_button_set_correctly(self) -> None:
        """Test chocolate set correctly."""
        item: CandyLandShake = CandyLandShake()
        item.chocolate = False
        panel: CandyPanel = CandyPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._chocolate.get(), is_(False))
        item.chocolate = True
        panel: CandyPanel = CandyPanel(PrimaryWindow(), item)
        assert_that(panel._chocolate.get(), is_(True))

    def test_strawberry_check_button(self) -> None:
        """Test strawberry check button."""
        item: CandyLandShake = CandyLandShake()
        panel: CandyPanel = CandyPanel(PrimaryWindow(), item)
        panel._strawberry.set(False)
        panel.action_performed("save")
        assert_that(item.strawberry, is_(False))
        panel._strawberry.set(True)
        panel.action_performed("save")
        assert_that(item.strawberry, is_(True))

    def test_strawberry_check_button_set_correctly(self) -> None:
        """Test strawberry set correctly."""
        item: CandyLandShake = CandyLandShake()
        item.strawberry = False
        panel: CandyPanel = CandyPanel(PrimaryWindow(), item)
        panel.action_performed("save")
        assert_that(panel._strawberry.get(), is_(False))
        item.strawberry = True
        panel: CandyPanel = CandyPanel(PrimaryWindow(), item)
        assert_that(panel._strawberry.get(), is_(True))

    def test_cancel_button(self) -> None:
        """Test the cancel button."""
        item: CandyLandShake = CandyLandShake()
        panel: CandyPanel = CandyPanel(PrimaryWindow(), item)
        panel._vanilla.set(False)
        panel._chocolate.set(False)
        panel._strawberry.set(False)
        panel.action_performed("cancel")
        unchanged: CandyLandShake = CandyLandShake()
        assert_that(item, is_(unchanged))
