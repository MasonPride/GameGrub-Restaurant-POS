"""Test file for SidePanel.

Author: Mason Pride
Version: 0.1
"""
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from src.gamegrub.data.sides.Side import Side
from src.gamegrub.data.enums.Size import Size
from src.gamegrub.gui.PrimaryWindow import PrimaryWindow
from src.gamegrub.gui.sides.SidePanel import SidePanel
from src.gamegrub.data.sides.Catan import CatanSkewers
from src.gamegrub.data.sides.Dice import PotatoDice
from src.gamegrub.data.sides.Risk import RiskBites
import pytest


class TestSidePanel:
    """Test Class for SidePanel."""

    @pytest.mark.parametrize("side", [PotatoDice(),
                                      RiskBites(),
                                      CatanSkewers()])
    def test_default_constructor(self, side: Side) -> None:
        """Test the default constructor."""
        panel: SidePanel = SidePanel(PrimaryWindow(), side)
        assert_that(panel._item, is_(side))

    def test_bad_action_command(self) -> None:
        """Test a bad action performed."""
        item = PotatoDice()
        panel: SidePanel = SidePanel(PrimaryWindow(), item)
        try:
            panel.action_performed("bad")
        except Exception:
            pytest.fail("Unexpected Exception")

    @pytest.mark.parametrize("size", Size)
    def test_base_combo_box(self, size: Size) -> None:
        """Test all bases combo box."""
        item: PotatoDice = PotatoDice()
        panel: SidePanel = SidePanel(PrimaryWindow(), item)
        panel._size.set(str(size))
        panel.action_performed("save")
        assert_that(item.size, is_(size))

    @pytest.mark.parametrize("size", Size)
    def test_base_combo_box_set_correctly(self, size: Size) -> None:
        """Test all bases combo box is correct."""
        item: PotatoDice = PotatoDice()
        item.size = size
        panel: SidePanel = SidePanel(PrimaryWindow(), item)
        assert_that(panel._size.get(), is_(str(size)))

    def test_cancel_button(self) -> None:
        """Test the cancel button."""
        item: PotatoDice = PotatoDice()
        panel: SidePanel = SidePanel(PrimaryWindow(), item)
        if item.size == Size.JUNIOR:
            panel._size.set(str(Size.WINNER))
        else:
            panel._size.set(str(Size.JUNIOR))
        panel.action_performed("cancel")
        unchanged: PotatoDice = PotatoDice()
        assert_that(item, is_(unchanged))
