import dataclasses

from ._suit import Suit


@dataclasses.dataclass(frozen=True, eq=True, order=True)
class Card:
    value: int
    suit: Suit
    name: str

    def __str__(self):
        return f"{self.name} of {self.suit}"

    def __int__(self):
        return self.value
