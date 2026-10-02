import random

from discount import Discount, NoDiscount


class OrderLine:
    """One menu item and how many of it were ordered."""

    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    @property
    def line_total(self):
        return self.item.price * self.quantity


class Order:
    """A customer's order: lines, discount, and totals."""

    def __init__(self):
        self.order_number = random.randint(1000, 9999)
        self._lines = {}  # item name -> OrderLine
        self._discount = NoDiscount()

    def add_item(self, item, quantity):
        """Add an item; repeated items have their quantities merged."""
        if item.name in self._lines:
            self._lines[item.name].quantity += quantity
        else:
            self._lines[item.name] = OrderLine(item, quantity)

    def apply_discount(self, discount: Discount):
        self._discount = discount

    @property
    def lines(self):
        return list(self._lines.values())

    @property
    def discount(self):
        return self._discount

    @property
    def subtotal(self):
        return sum(line.line_total for line in self._lines.values())

    @property
    def discount_amount(self):
        return self._discount.compute(self.subtotal)

    @property
    def total_due(self):
        return self.subtotal - self.discount_amount