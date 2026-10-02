"""Pure calculation functions. No input() or print() here."""

from config import SC_PWD_DISCOUNT_RATE


def calculate_subtotal(customer_orders, menu):
    return sum(menu[name] * quantity for name, quantity in customer_orders.items())


def calculate_discount(subtotal, is_eligible):
    return subtotal * SC_PWD_DISCOUNT_RATE if is_eligible else 0.0


def calculate_total(subtotal, discount_amount):
    return subtotal - discount_amount


def is_cash_sufficient(cash_tendered, total_due):
    return round(cash_tendered, 2) >= round(total_due, 2)


def calculate_change(cash_tendered, total_due):
    return cash_tendered - total_due