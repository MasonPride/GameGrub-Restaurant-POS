"""Menu Controller class.

Creates the menu controller for our web app.

Author: Mason Pride
Version: 0.1
"""
from flask import render_template, request
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

    @route('/advancedsearch/', methods=['GET'])
    def advanced_search(self):
        """Display advanced search."""
        return render_template("advanced_search.html",
                                entree=True, side=True,
                                drink=True, combo=True)

    @route('/advancedsearch/', methods=['POST'])
    def advanced_search_results(self):
        """Display advanced search results."""
        keyword: str = request.form.get('keyword', None)
        entree: bool = bool(request.form.get('entree', False))
        side: bool = bool(request.form.get('side', False))
        drink: bool = bool(request.form.get('drink', False))
        combo: bool = bool(request.form.get('combo', False))
        try:
            pricemin: float = float(request.form.get('pricemin', "-1"))
        except Exception:
            pricemin = -1
        try:
            pricemax: float = float(request.form.get('pricemax', "-1"))
        except Exception:
            pricemax = -1
        try:
            caloriesmin: int = int(request.form.get('caloriesmin', "-1"))
        except Exception:
            caloriesmin = -1
        try:
            caloriesmax: int = int(request.form.get('caloriesmax', "-1"))
        except Exception:
            caloriesmax = -1

        menu = Menu.full_menu()
        menu = Menu.filter_keywords(menu, keyword)
        menu = Menu.filter_type(menu, entree, side, drink, combo)
        menu = Menu.filter_price(menu, pricemin, pricemax)
        menu = Menu.filter_calories(menu, caloriesmin, caloriesmax)

        return render_template("advanced_search.html", keyword=keyword,
                                menu=menu, entree=entree,
                                side=side, drink=drink, combo=combo,
                                pricemin=("" if pricemin < 0 else pricemin),
                                pricemax=("" if pricemax < 0 else pricemax),
                                caloriesmin=("" if caloriesmin < 0 else caloriesmin),
                                caloriesmax=("" if caloriesmax < 0 else caloriesmax))
