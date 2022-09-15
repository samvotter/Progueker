import dataclasses
import typing


@dataclasses.dataclass(frozen=True, order=True)
class Suit:

    name: str
    color: str

    def __str__(self):
        return self.name


@dataclasses.dataclass(frozen=True, order=True)
class Card:

    suit: Suit
    value: int
    name: str

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

        This is the generally accepted composition of a deck of cards. However, a deck of cards is not limited to
        those parameters. A deck may have any arbitrary number of cards in whatever distribution is provided.

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


class StandardDeck(Deck):

    def __init__(self):
        """
        A standard playing card deck has:
            52 Cards divided into:
                4 suits: Diamonds, Clubs, Hearts, and Spades
                Within each suit there are:
                    9 numbered cards: from 2-10
                    4 face cards: Jack, Queen, King, Ace
        """
        suits = [
            Suit(name="Clubs",      color="Black"),
            Suit(name="Diamonds",   color="Red"),
            Suit(name="Hearts",     color="Red"),
            Suit(name="Spades",     color="Black")
        ]
        card_values = [
            (2, "Two"),
            (3, "Three"),
            (4, "Four"),
            (5, "Five"),
            (6, "Six"),
            (7, "Seven"),
            (8, "Eight"),
            (9, "Nine"),
            (10, "Ten"),
            (11, "Jack"),
            (12, "Queen"),
            (13, "King"),
            (14, "Ace")
        ]
        cards = [
            Card(suit=suit, value=card_value[0], name=card_value[1])
            for card_value in card_values
            for suit in suits
        ]
        super().__init__(cards=cards)
