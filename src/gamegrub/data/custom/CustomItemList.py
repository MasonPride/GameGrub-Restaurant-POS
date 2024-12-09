"""Custom item list class.

Author: Mason Pride
Version: 0.1
"""
from typing import Iterator, Iterable, List, Optional
from src.gamegrub.data.custom.CustomItem import CustomItem
import json


class CustomItemList(Iterable[CustomItem]):
    """Custom Item List class."""

    _instance: Optional["CustomItemList"] = None

    def __init__(self) -> None:
        """Empty constructor."""
        pass

    def __new__(cls) -> 'CustomItemList':
        """Hijack new method to return singleton."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.load()
        return cls._instance

    def load(self) -> None:
        """Loads the empty list."""
        self.__items: List[CustomItem] = list()
        """Load data."""
        with open('custom_menu_items.json') as file:
            array = json.load(file)
            self.__items: List[CustomItem] = list()
            for item in array:
                custom_item = CustomItem()
                custom_item.load(**item)
                self.__items.append(custom_item)

    def add_item(self, item: CustomItem) -> None:
        """Adds custom item to list."""
        self.__items.append(item)

    def __iter__(self) -> Iterator[CustomItem]:
        """Returns iterator of movies."""
        return iter(self.__items)

    def __len__(self) -> int:
        """Returns length of movies."""
        return len(self.__items)

    def __getitem__(self, i: int) -> CustomItem:
        """Get a single custom item."""
        return self.__items[i]

    def __setitem__(self, i: int, item: CustomItem) -> None:
        """Set a single custom item."""
        self.__items[i] = item

    def __delitem__(self, i: int) -> None:
        """Delete a single custom item."""
        del self.__items[i]

    def save(self) -> None:
        """Saves custom item list content."""
        array = list()
        for custom_item in CustomItemList():
            item_dict = dict()
            item_dict['Name'] = str(custom_item.name)
            item_dict['Price'] = float(custom_item.price)
            item_dict['Calories'] = int(custom_item.calories)
            array.append(item_dict)

        with open("custom_menu_items.json", "w") as file:
                json.dump(array, file, indent=4)
