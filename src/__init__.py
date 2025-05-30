"""Meta package for all project packages.

This is the __init__ file for this package.

Typically this file can be left blank, but for this example we have
included a print statement so we can see what it does and when.

Usage:
    python3 -m src - execute this program (when run from project root).

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
from src.gamegrub.Web import Web

print("In /src/__init__.py")
app = Web.main(list())