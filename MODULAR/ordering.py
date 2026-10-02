"""Builds the customer's order from user input."""

from inputs import ask_yes_no, get_menu_choice, get_valid_quantity


def take_customer_orders(menu):
    """Return a dict of {item name: quantity}."""
    customer_orders = {}
    while True:
        item = get_menu_choice(menu)
        quantity = get_valid_quantity()

        customer_orders[item] = customer_orders.get(item, 0) + quantity
        print(f">> Added: {quantity} x {item}\n")

        if not ask_yes_no("Order another item? (y/n): "):
            print()
            return customer_orders
        print()