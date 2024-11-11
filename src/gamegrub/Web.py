"""Web class for gamegrub.

This class will run the web app.

Author: Mason Pride
Version: 0.1
"""
from flask import Flask
from src.gamegrub.web.MenuController import MenuController
from typing import List


class Web:
    """Web class."""

    @staticmethod
    def main(args: List[str]):
        """Main method."""
        app = Flask(__name__)
        MenuController.register(app)
        return app
