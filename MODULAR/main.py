"""Entry point: wires the modules together."""

import random

from calculations import (calculate_change, calculate_discount,
                          calculate_subtotal, calculate_total,
                          is_cash_sufficient)
from config import MENU
from display import display_menu, print_receipt
from inputs import ask_yes_no, get_cash_tendered
from ordering import take_customer_orders


def collect_payment(total_due):
    """Keep asking until the cash covers the total. Returns (cash, change)."""
    while True:
        cash = get_cash_tendered(total_due)
        if is_cash_sufficient(cash, total_due):
            return cash, calculate_change(cash, total_due)
        print(">> Insufficient cash. Please enter an amount equal to or greater than the total.\n")


def main():
    print()
    display_menu(MENU)

    wants_to_order = ask_yes_no("\nWould you like to order? (y/n): ")
    print()
    if not wants_to_order:
        print("Thank you for visiting. Goodbye!")
        return

    customer_orders = take_customer_orders(MENU)

    subtotal = calculate_subtotal(customer_orders, MENU)
    is_eligible = ask_yes_no("Senior Citizen / PWD with valid ID? (y/n): ")
    print()
    discount_amount = calculate_discount(subtotal, is_eligible)
    total_due = calculate_total(subtotal, discount_amount)

    cash_tendered, change = collect_payment(total_due)
    order_number = random.randint(1000, 9999)

    print_receipt(customer_orders, MENU, subtotal, discount_amount,
                  total_due, cash_tendered, change, order_number)


if __name__ == "__main__":
    main()