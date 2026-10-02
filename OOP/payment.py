class Payment:
    """Handles cash tendered against an amount due."""

    def __init__(self, amount_due):
        self.amount_due = amount_due
        self.cash_tendered = 0.0

    def tender(self, cash):
        """Record the cash if sufficient. Returns True on success."""
        if round(cash, 2) < round(self.amount_due, 2):
            return False
        self.cash_tendered = cash
        return True

    @property
    def change(self):
        return self.cash_tendered - self.amount_due