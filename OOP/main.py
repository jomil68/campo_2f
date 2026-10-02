from config import MENU_DATA, STORE_ADDRESS, STORE_NAME, STORE_TIN
from input_handler import InputHandler
from kiosk import OrderingKiosk
from menu import Menu
from store import Store


def main():
    store = Store(STORE_NAME, STORE_ADDRESS, STORE_TIN)
    menu = Menu.from_dict(MENU_DATA)
    kiosk = OrderingKiosk(store, menu, InputHandler())
    kiosk.run()


if __name__ == "__main__":
    main()