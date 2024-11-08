"""Selection Dialog class.

Creates the selection dialog box.

Author: Mason Pride
Version: 0.1
"""
from tkinter import Button, Label
from tkinter.simpledialog import Dialog  # type: ignore
from typing import List, Optional


class SelectionDialog(Dialog):
    """Selection Dialog class."""
    def __init__(self, master, title: str = "Selection",
                 message: str = "Select and option",
                 options: List[str] = ["Yes", "No", "Cancel"]) -> None:
        """Selection Dialog contructor."""
        self.__message = message
        self.__options = options
        self.result: Optional[str] = None
        super().__init__(master, title)

    def body(self, master) -> None:
        """Body method."""
        message = Label(master=master, text=self.__message)
        message.grid(row=0, column=0, columnspan=len(self.__options),
                     padx=2, pady=2, sticky="EW")
        i: int = 0
        for option in self.__options:
            button = Button(master=master, text=option,
                            command=lambda x=option: self.action_performed(x))
            button.grid(row=1, column=i, padx=2, pady=2, sticky="EW")
            i += 1

    def buttonbox(self) -> None:
        """Button box method."""
        pass

    def action_performed(self, text: str) -> None:
        """Action Performed method."""
        self.result = text
        self.destroy()
