from dataclasses import dataclass


@dataclass(frozen=True)
class Store:
    """Store details printed on the menu and receipt."""
    name: str
    address: str
    tin: str