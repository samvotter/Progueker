import dataclasses
import typing


@dataclasses.dataclass(frozen=True, order=True)
class Suit:

    name: str
    color: str


@dataclasses.dataclass(frozen=True, order=True)
class Card:

    suit: Suit
    name: str
    value: int

    def __str__(self):
        return f"{self.name} of {self.suit}"

    def __int__(self):
        return self.value


class Deck:

    def __init__(
            self,
            cards: typing.List[Card]
    ):
        """
        A deck is solely comprised of Cards. A standard playing card deck has:
            52 Cards divided into:
                4 suits: Diamonds, Clubs, Hearts, and Spades
                Within each suit there are:
                    9 numbered cards: from 2-10
                    4 face cards: Jack, Queen, King, Ace

        This is the generally accepted composition of a deck of cards. However a deck of cards does not limit itself to
        those parameters. A deck may have any arbitrary number of cards in whatever distribution is provided.

        The stack are the cards that will be dealt out over the course of the game to the players. Cards will leave
            the stack once they are drawn.

        :param cards: A list of Card objects
        """
        self._iter_idx = 0
        self.stack = cards

    def __len__(self):
        return len(self.stack)

    def __iter__(self):
        self._iter_idx = 0
        return self

    def __next__(self):
        if self._iter_idx >= len(self):
            raise StopIteration
        self._iter_idx += 1
        return self.stack[self._iter_idx - 1]

    def draw(self):
        return self.stack.pop()
