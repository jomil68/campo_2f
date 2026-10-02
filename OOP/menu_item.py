from dataclasses import dataclass


@dataclass(frozen=True)
class MenuItem:
    """A single sellable item."""
    name: str
    price: float