import abc

from progueker.game_tokens import Card


class Dealer(abc.ABC):
    """
    The Dealer's single responsibility is to deal cards.
    """

    @abc.abstractmethod
    def shuffle_deck(self, deck: list[Card]) -> None:
        """
        Given a collection of cards, manipulate their order.
        """
        pass

    @abc.abstractmethod
    def draw_from_deck(self, deck: list[Card]) -> Card:
        """
        Given a deck of cards, draw a card from it.
        """
        pass

    @abc.abstractmethod
    def collect_cards(self, cards: list[Card]) -> None:
        """
        Take cards from the table.
        """
