import typing
import random

from progueker.game_tokens import decks
from progueker.game_tokens import cards

from progueker.dealers import dealer


class StandardDealer(dealer.Dealer):
    """
    The StandardDealer's single responsibility is to deal cards in a neutral, impartial way.
    """

    def __init__(self):
        self.deck = decks.StandardDeck()

    def shuffle_deck(self, deck: decks.Deck) -> None:
        random.shuffle(deck)

    def draw_from_deck(self, deck: decks.Deck) -> cards.Card:
        try:
            return deck.pop()
        except IndexError:
            raise dealer.RanOutOfCards(f"Cannot draw from {deck}, there are no more cards.")

    def collect_card(self,  deck: decks.Deck, tray: typing.List[cards.Card]) -> None:
        while cards:
            deck.append(tray.pop())
