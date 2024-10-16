"""Main class for gamegrub.

This class will load and display the programs gui.

Author: Mason Pride
Version: 0.1
"""
from typing import List
from src.gamegrub.gui.PrimaryWindow import PrimaryWindow


class Main:
    """Main Class."""

    @staticmethod
    def main(args: List[str]) -> None:
        """Main method."""
        PrimaryWindow().mainloop()
