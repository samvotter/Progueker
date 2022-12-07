import typing

from progueker.game_tokens.cards import StandardSuits, Card


class Deck(list):

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
        super().__init__(cards)


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
        suits = [StandardSuits().values()]
        card_values = [
            (2,     "Two"),
            (3,     "Three"),
            (4,     "Four"),
            (5,     "Five"),
            (6,     "Six"),
            (7,     "Seven"),
            (8,     "Eight"),
            (9,     "Nine"),
            (10,    "Ten"),
            (11,    "Jack"),
            (12,    "Queen"),
            (13,    "King"),
            (14,    "Ace")
        ]
        cards = [
            Card(suit=suit, value=card_value, name=card_name)
            for card_value, card_name in card_values
            for suit in suits
        ]
        super().__init__(cards=cards)
