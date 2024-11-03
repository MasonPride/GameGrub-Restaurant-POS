"""Drink base class.

Creates the frame base for Drink classes

Author: Mason Pride
Version: 0.1
"""
from tkinter import Frame


class DrinkPanel(Frame):
    """Drink Panel class."""
    def __init__(self, master) -> None:
        """Initialize frame."""
        Frame.__init__(self, master=master)

    def action_performed(self, text: str) -> None:
        """Action performed method."""
        pass
