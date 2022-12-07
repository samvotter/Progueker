import dataclasses

from progueker.consts import Colors
from progueker.utils import EnumDict


@dataclasses.dataclass(frozen=True, order=True)
class Suit:

    """
    A suit's single responsibility is to identify a card as belonging to a set of other matching suits.
    """

    name: str
    color: str

    def __str__(self):
        return self.name


class StandardSuits(EnumDict):
    HEARTS = Suit(name="Hearts", color=Colors.RED)
    CLUBS = Suit(name="Clubs", color=Colors.BLACK)
    DIAMONDS = Suit(name="Diamonds", color=Colors.RED)
    SPADES = Suit(name="Spades", color=Colors.BLACK)


@dataclasses.dataclass(order=True)
class Card:

    suit: Suit
    value: int
    name: str

    def __str__(self):
        return f"{self.name} of {self.suit}"

    def __int__(self):
        return self.value
