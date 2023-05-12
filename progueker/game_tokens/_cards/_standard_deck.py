from ._card import Card
from ._standard_suits import StandardSuits


class StandardDeck(list):

    def __init__(self):
        """
        A standard playing card deck has:
            52 Cards divided into:
                4 suits: Diamonds, Clubs, Hearts, and Spades
                Within each suit there are:
                    9 numbered cards: from 2-10
                    4 face cards: Jack, Queen, King, Ace
        """
        suits = list(StandardSuits)
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
        super().__init__(cards)


my_deck = StandardDeck()
pass
