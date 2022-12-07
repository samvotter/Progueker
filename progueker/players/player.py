import abc


class Player(abc.ABC):
    """
    The Player's single responsibility is to represent a poker player
    """

    # bidding actions
    @abc.abstractmethod
    def fold(self):
        """
        This action takes players out of a round.
        """
        pass

    @abc.abstractmethod
    def call(self):
        """
        This action requires the player to contribute a number of chips equal to the current bid into the pot.
        """
        pass

    @abc.abstractmethod
    def raise_bid(self):
        """
        This action requires the player to contribute MORE chips into the pot than is required to match the current bid.
        """
        pass

    # hand actions
    @abc.abstractmethod
    def request_card(self):
        """
        Request additional cards. Typically, players need more cards when:
            * being dealt a new round
            * when they wish to exchange cards in their hand for other cards
        It should be left to the implementation of the player class to determine how/when/why that player chooses
        to request more cards
        """
        pass

    @abc.abstractmethod
    def discard_card(self):
        """
        Relinquish a card.
        """
