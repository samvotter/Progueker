import actors
import game_tokens
import card_objects
import typing


class PokerSetup:
    """
    PokerSetup's single responsibility is to organize all the elements required for a game of poker
    """

    def __init__(
            self,
            players: typing.List[actors.Player],
            chips: typing.List[game_tokens.Chip],
            deck: card_objects.Deck = None,
    ):
        self.players = players
        self.banker = actors.Banker(chips=chips)
        deck = deck or card_objects.StandardDeck()
        self.dealer = actors.Dealer(deck=deck)

    def __str__(self):
        for player in self.players:
            print(player)
