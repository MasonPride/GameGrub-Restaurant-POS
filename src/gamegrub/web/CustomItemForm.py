"""Custom Item Form Class."""
from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField,
                     DecimalField, validators)
from wtforms.widgets import NumberInput
import decimal


class CustomItemForm(FlaskForm):
    """Custom item form."""
    name = StringField("Name", [validators.Length(min=4)])
    price = DecimalField("Price",
                         [validators.NumberRange(min=1.50, max=100)],
                         default=0,
                         places=2,
                         rounding=decimal.ROUND_HALF_UP,
                         widget=NumberInput(step=0.01))
    calories = IntegerField("Calories",
                            [validators.NumberRange(min=250, max=10000)],
                            default=0,
                            widget=NumberInput(step=1))
