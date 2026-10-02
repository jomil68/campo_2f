"""Console input functions with validation. No calculations here."""


def ask_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ("y", "yes"):
            return True
        if response in ("n", "no"):
            return False
        print(">> Invalid input. Please answer with 'y' or 'n'.\n")


def get_menu_choice(menu):
    """Return the name of the chosen menu item."""
    item_names = list(menu.keys())
    total_items = len(item_names)
    while True:
        raw = input(f"Enter item number (1-{total_items}): ").strip()
        if not raw.isdigit():
            print(">> Invalid input. Please enter a whole number.\n")
            continue
        number = int(raw)
        if number < 1 or number > total_items:
            print(f">> Invalid choice. Please enter a number from 1 to {total_items}.\n")
            continue
        return item_names[number - 1]


def get_valid_quantity():
    while True:
        raw = input("Enter quantity: ").strip()
        if not raw.isdigit() or int(raw) == 0:
            print(">> Invalid input. Quantity must be a whole number greater than 0.\n")
            continue
        return int(raw)


def get_cash_tendered(total_due):
    """Return a valid number entered as cash (sufficiency is checked elsewhere)."""
    while True:
        raw = input(f"Total due: P{total_due:.2f}\nCash tendered: P").strip()
        try:
            return float(raw)
        except ValueError:
            print(">> Invalid input. Please enter a valid amount.\n")