"""Custom Item Form Class."""
from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField,
                     DecimalField)
from wtforms.widgets import NumberInput


class CustomItemForm(FlaskForm):
    """Custom item form."""
    name = StringField("Name")
    price = DecimalField("Price",
                         default=0,
                         places=2,
                         widget=NumberInput(min=0, max=30, step=0.01))
    calories = IntegerField("Calories",
                            default=0,
                            widget=NumberInput(min=0, max=2500, step=1))
