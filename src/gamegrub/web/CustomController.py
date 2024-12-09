"""Controller for Custom Items.

Author: Mason Pride
Version: 0.1
"""
from flask import render_template, redirect
from flask_classful import FlaskView, route  # type: ignore
from src.gamegrub.data.custom.CustomItem import CustomItem
from src.gamegrub.data.custom.CustomItemList import CustomItemList
from src.gamegrub.web.CustomItemForm import CustomItemForm


class CustomController(FlaskView):
    """Controller for Custom Items."""

    route_base = "/custom/"

    @route('/')
    def index(self):
        """Display list of items."""
        items = CustomItemList()
        return render_template("custom_menu.html", items=items)

    @route('/<id>/', methods=['GET'])
    def single(self, id: int):
        """Display single item."""
        items = CustomItemList()
        print(len(items))
        item = items[int(id)]
        return render_template("single_item.html", item=item, id=id)

    @route('/<id>/edit/', methods=['GET'])
    def edit_form(self, id: int):
        """Edit form for item."""
        items = CustomItemList()
        item = items[int(id)]
        form = CustomItemForm(obj=item)
        return render_template("edit_form.html", form=form, id=id)

    @route('/<id>/', methods=['POST'])
    def edit(self, id: int):
        """Edit post."""
        form = CustomItemForm()
        if not form.validate_on_submit():
            return render_template("edit_form.html", form=form, id=id)
        items = CustomItemList()
        item = CustomItem()
        item.name = form.name.data
        try:
            item.price = float(form.price.data)
        except Exception:
            item.price = None
        try:
            item.calories = int(
                form.calories.data)
        except Exception:
            item.calories = None

        items[int(id)] = item
        return redirect('/custom/')

    @route('/<id>/delete/', methods=['GET'])
    def delete_form(self, id: int):
        """Displays delete form."""
        items = CustomItemList()
        item = items[int(id)]
        return render_template("delete_form.html", item=item, id=id)

    @route('/<id>/delete/', methods=['POST'])
    def delete(self, id: int):
        """Delete POST."""
        items = CustomItemList()
        del items[int(id)]
        return redirect('/custom/')

    @route('/new/', methods=['GET'])
    def new_form(self):
        """New item form."""
        item = CustomItem()
        form = CustomItemForm(obj=item)
        return render_template("new_form.html", form=form)

    @route('/', methods=['POST'])
    def add_item(self):
        """Adds item to custom item menu."""
        form = CustomItemForm()
        if not form.validate_on_submit():
            return render_template("edit_form.html", form=form, id=id)
        items = CustomItemList()
        item = CustomItem()
        item.name = form.name.data
        try:
            item.price = float(form.price.data)
        except Exception:
            item.price = None
        try:
            item.calories = int(
                form.calories.data)
        except Exception:
            item.calories = None
        items.add_item(item)
        return redirect('/custom/')

    @route('/save/', methods=['POST'])
    def save(self):
        CustomItemList().save()
        return redirect('/custom/')