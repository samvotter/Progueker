import enum

from progueker.consts import Colors

from ._suit import Suit


class StandardSuits(Suit, enum.Enum):
    SPADES = (4, "Spades", Colors.BLACK)
    HEARTS = (3, "Hearts", Colors.RED)
    DIAMONDS = (2, "Diamonds", Colors.RED)
    CLUBS = (1, "Clubs", Colors.BLACK)
