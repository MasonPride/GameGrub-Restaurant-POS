"""Menu Controller class.

Creates the menu controller for our web app.

Author: Mason Pride
Version: 0.1
"""
from flask import render_template
from flask_classful import FlaskView, route  # type: ignore
from src.gamegrub.data.menu.Menu import Menu
from src.gamegrub.data.combo.Combo import Combo


class MenuController(FlaskView):
    """MenuController class."""
    route_base = "/"

    @route('/')
    def index(self):
        """Index route method.

        Defines the route for index.

        Returns:
            render template of index
        """
        return render_template("index.html")

    @route('/about/')
    def about(self):
        """About route method.

        Defines the route for about.

        Returns:
            render template of about
        """
        return render_template("about.html")

    @route('/menu/')
    def menu(self):
        """Menu route method.

        Defines the route for menu.

        Returns:
            render template of menu
        """
        menu = Menu()
        combo = Combo()
        return render_template("menu.html",
                               menu=menu,
                               discount=combo.get_discount())
