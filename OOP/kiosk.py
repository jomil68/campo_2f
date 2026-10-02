from config import RECEIPT_WIDTH
from discount import SeniorPWDDiscount
from order import Order
from payment import Payment
from receipt import Receipt


class OrderingKiosk:
    """Coordinates the whole ordering flow."""

    def __init__(self, store, menu, input_handler):
        self.store = store
        self.menu = menu
        self.input = input_handler

    def run(self):
        print()
        self.menu.display(self.store.name + " MENU", RECEIPT_WIDTH)

        wants_to_order = self.input.ask_yes_no("\nWould you like to order? (y/n): ")
        print()
        if not wants_to_order:
            print("Thank you for visiting. Goodbye!")
            return

        order = self._take_order()
        self._apply_discount(order)
        payment = self._take_payment(order)
        Receipt(self.store, order, payment).print()

    def _take_order(self):
        order = Order()
        while True:
            number = self.input.get_menu_choice(self.menu)
            quantity = self.input.get_quantity()
            item = self.menu.get_by_number(number)
            order.add_item(item, quantity)
            print(f">> Added: {quantity} x {item.name}\n")

            more = self.input.ask_yes_no("Order another item? (y/n): ")
            print()
            if not more:
                return order

    def _apply_discount(self, order):
        eligible = self.input.ask_yes_no("Senior Citizen / PWD with valid ID? (y/n): ")
        print()
        if eligible:
            order.apply_discount(SeniorPWDDiscount())

    def _take_payment(self, order):
        payment = Payment(order.total_due)
        while True:
            cash = self.input.get_cash_amount(payment.amount_due)
            if payment.tender(cash):
                return payment
            print(">> Insufficient cash. Please enter an amount equal to or greater than the total.\n")