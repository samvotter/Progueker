import abc
import typing

from progueker.game_tokens import decks
from progueker.game_tokens import cards


class Dealer(abc.ABC):
    """
    The Dealer's single responsibility is to deal cards.
    """

    @abc.abstractmethod
    def shuffle_deck(self, deck: decks.Deck) -> None:
        """
        Given a collection of cards, manipulate their order.
        """
        pass

    @abc.abstractmethod
    def draw_from_deck(self, deck: decks.Deck) -> cards.Card:
        """
        Given a deck of cards, draw a card from it.
        """
        pass

    @abc.abstractmethod
    def collect_card(self,  deck: decks.Deck, card: cards.Card) -> decks.Deck:
        """
        Given a bunch of cards, organize them into a deck
        """
        pass


class DealerExceptions(Exception):
    pass


class RanOutOfCards(DealerExceptions):
    pass