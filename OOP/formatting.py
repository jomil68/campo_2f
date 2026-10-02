"""Small console formatting helpers shared by the menu and the receipt."""


def print_header(title, width):
    print("=" * width)
    print(title.center(width))
    print("=" * width)


def print_divider(width, char="-"):
    print(char * width)