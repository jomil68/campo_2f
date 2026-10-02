import datetime

from config import RECEIPT_WIDTH


class Receipt:
    """Builds and prints the official receipt for a paid order."""

    def __init__(self, store, order, payment, issued_at=None, width=RECEIPT_WIDTH):
        self.store = store
        self.order = order
        self.payment = payment
        self.issued_at = issued_at or datetime.datetime.now()
        self.width = width

    def render(self):
        w = self.width
        o = self.order
        lines = [
            "",
            "=" * w,
            self.store.name.center(w),
            self.store.address.center(w),
            f"TIN: {self.store.tin}".center(w),
            "=" * w,
            f"Order No.: {o.order_number}",
            f"Date: {self.issued_at.strftime('%m/%d/%Y')}  "
            f"Time: {self.issued_at.strftime('%I:%M %p')}",
            "-" * w,
            f"{'QTY':<4}{'ITEM':<22}{'PRICE':>7}{'TOTAL':>9}",
            "-" * w,
        ]

        for line in o.lines:
            name = line.item.name
            display_name = name if len(name) <= 22 else name[:19] + "..."
            lines.append(
                f"{line.quantity:<4}{display_name:<22}"
                f"{line.item.price:>7.2f}{line.line_total:>9.2f}"
            )

        lines.append("-" * w)
        lines.append(f"{'SUBTOTAL':<33}{o.subtotal:>9.2f}")
        if o.discount_amount > 0:
            lines.append(
                f"{o.discount.label:<33}{'-' + format(o.discount_amount, '.2f'):>9}"
            )
        lines.append(f"{'TOTAL DUE':<33}{o.total_due:>9.2f}")
        lines.append(f"{'CASH':<33}{self.payment.cash_tendered:>9.2f}")
        lines.append(f"{'CHANGE':<33}{self.payment.change:>9.2f}")
        lines += [
            "=" * w,
            "Thank you for dining with us!".center(w),
            "Please come again.".center(w),
            "=" * w,
        ]
        return "\n".join(lines)

    def print(self):
        print(self.render())