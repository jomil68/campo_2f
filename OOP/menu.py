from formatting import print_header, print_divider
from menu_item import MenuItem


class Menu:
    """A numbered collection of MenuItem objects."""

    def __init__(self, items):
        self._items = list(items)

    @classmethod
    def from_dict(cls, data):
        return cls(MenuItem(name, price) for name, price in data.items())

    def __len__(self):
        return len(self._items)

    def get_by_number(self, number):
        """Return the item for a 1-based menu number."""
        return self._items[number - 1]

    def display(self, title, width):
        print_header(title, width)
        for number, item in enumerate(self._items, start=1):
            print(f"{number:>2}. {item.name:<28} P{item.price:>7.2f}")
        print_divider(width)