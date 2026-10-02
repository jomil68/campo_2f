class InputHandler:
    """All console input and validation lives here."""

    def ask_yes_no(self, prompt):
        while True:
            response = input(prompt).strip().lower()
            if response in ("y", "yes"):
                return True
            if response in ("n", "no"):
                return False
            print(">> Invalid input. Please answer with 'y' or 'n'.\n")

    def get_menu_choice(self, menu):
        """Return a valid 1-based menu number."""
        total = len(menu)
        while True:
            raw = input(f"Enter item number (1-{total}): ").strip()
            if not raw.isdigit():
                print(">> Invalid input. Please enter a whole number.\n")
                continue
            number = int(raw)
            if number < 1 or number > total:
                print(f">> Invalid choice. Please enter a number from 1 to {total}.\n")
                continue
            return number

    def get_quantity(self):
        while True:
            raw = input("Enter quantity: ").strip()
            if not raw.isdigit() or int(raw) == 0:
                print(">> Invalid input. Quantity must be a whole number greater than 0.\n")
                continue
            return int(raw)

    def get_cash_amount(self, total_due):
        while True:
            raw = input(f"Total due: P{total_due:.2f}\nCash tendered: P").strip()
            try:
                return float(raw)
            except ValueError:
                print(">> Invalid input. Please enter a valid amount.\n")