from abc import ABC, abstractmethod

from config import SC_PWD_DISCOUNT_RATE


class Discount(ABC):
    """Base class for all discounts (add new ones by subclassing)."""

    @property
    @abstractmethod
    def label(self):
        """Text shown on the receipt."""

    @abstractmethod
    def compute(self, subtotal):
        """Return the discount amount for the given subtotal."""


class NoDiscount(Discount):
    @property
    def label(self):
        return "NO DISCOUNT"

    def compute(self, subtotal):
        return 0.0


class SeniorPWDDiscount(Discount):
    def __init__(self, rate=SC_PWD_DISCOUNT_RATE):
        self._rate = rate

    @property
    def label(self):
        return f"SC/PWD DISCOUNT ({self._rate:.0%})"

    def compute(self, subtotal):
        return subtotal * self._rate