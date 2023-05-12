import random

from progueker.game_tokens import Card, StandardDeck, RanOutOfCardsException
from ._dealer import Dealer


class StandardDealer(Dealer):
    """
    The StandardDealer's single responsibility is to deal cards in an impartial way.
    """

    def __init__(self):
        self.deck = StandardDeck()

    def shuffle_deck(self, deck: list[Card]) -> None:
        random.shuffle(list(deck))

    def draw_from_deck(self, deck: list[Card]) -> Card:
        try:
            return deck.pop()
        except IndexError:
            raise RanOutOfCardsException(f"Dealer cannot deal any more cards")

    def collect_cards(self, cards: list[Card]) -> None:
        [self.deck.append(cards.pop()) for _ in cards]
