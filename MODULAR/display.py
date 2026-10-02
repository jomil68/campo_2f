"""All screen output: the menu and the receipt."""

import datetime

from config import RECEIPT_WIDTH, STORE_ADDRESS, STORE_NAME, STORE_TIN


def print_header(title):
    print("=" * RECEIPT_WIDTH)
    print(title.center(RECEIPT_WIDTH))
    print("=" * RECEIPT_WIDTH)


def display_menu(menu):
    print_header(STORE_NAME + " MENU")
    for number, (name, price) in enumerate(menu.items(), start=1):
        print(f"{number:>2}. {name:<28} P{price:>7.2f}")
    print("-" * RECEIPT_WIDTH)


def print_receipt(customer_orders, menu, subtotal, discount_amount,
                  total_due, cash_tendered, change, order_number):
    now = datetime.datetime.now()
    print()
    print("=" * RECEIPT_WIDTH)
    print(STORE_NAME.center(RECEIPT_WIDTH))
    print(STORE_ADDRESS.center(RECEIPT_WIDTH))
    print(f"TIN: {STORE_TIN}".center(RECEIPT_WIDTH))
    print("=" * RECEIPT_WIDTH)
    print(f"Order No.: {order_number}")
    print(f"Date: {now.strftime('%m/%d/%Y')}  Time: {now.strftime('%I:%M %p')}")
    print("-" * RECEIPT_WIDTH)
    print(f"{'QTY':<4}{'ITEM':<22}{'PRICE':>7}{'TOTAL':>9}")
    print("-" * RECEIPT_WIDTH)

    for name, quantity in customer_orders.items():
        unit_price = menu[name]
        display_name = name if len(name) <= 22 else name[:19] + "..."
        print(f"{quantity:<4}{display_name:<22}{unit_price:>7.2f}{unit_price * quantity:>9.2f}")

    print("-" * RECEIPT_WIDTH)
    print(f"{'SUBTOTAL':<33}{subtotal:>9.2f}")
    if discount_amount > 0:
        print(f"{'SC/PWD DISCOUNT (20%)':<33}{'-' + format(discount_amount, '.2f'):>9}")
    print(f"{'TOTAL DUE':<33}{total_due:>9.2f}")
    print(f"{'CASH':<33}{cash_tendered:>9.2f}")
    print(f"{'CHANGE':<33}{change:>9.2f}")
    print("=" * RECEIPT_WIDTH)
    print("Thank you for dining with us!".center(RECEIPT_WIDTH))
    print("Please come again.".center(RECEIPT_WIDTH))
    print("=" * RECEIPT_WIDTH)