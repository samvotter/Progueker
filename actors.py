import card_objects
import game_tokens
import random
import typing
import hands


class Player:
    """
    The Player's single responsibility is to play the game.
    """
    def __init__(
            self,
            name: str,
            chips: typing.List[game_tokens.Chip],
            hand: hands.Hand,
    ):
        self.name = name
        self.chips = chips
        self.hand = hand


class Dealer:
    """
    The Dealer's single responsibility is to deal cards.
    """

    def __init__(
            self,
            deck: card_objects.Deck,
    ):
        self.deck = deck

    def shuffle(self, cards: typing.List[card_objects.Card] = None):
        if cards is None:
            cards = self.deck
        random.shuffle(cards)

    def draw_from_deck(self, deck: card_objects.Deck = None):
        if deck is None:
            deck = self.deck
        return deck.stack.pop()

    def deal_hands(self, hands_to_be_dealt: typing.List[hands.Hand], deck: card_objects.Deck = None):
        if deck is None:
            deck = self.deck
        while hands_to_be_dealt:
            for hand in hands_to_be_dealt:
                drawn_card = self.draw_from_deck(deck)
                hand.cards.append(drawn_card)
            hands_to_be_dealt = list(filter(lambda x: len(x.cards) < x.max_size, hands_to_be_dealt))

    def add_cards_to_deck(self, cards: typing.List[card_objects.Card], deck: card_objects.Deck = None):
        if deck is None:
            deck = self.deck
        while cards:
            deck.stack.append(cards.pop())


class BankerExceptions(Exception):
    pass


class NotExactChange(BankerExceptions):

    def __init__(self, msg: str, chips_needed: int, remaining: int):
        self.msg = msg
        self.chips_needed = chips_needed
        self.remaining = remaining
        super().__init__(msg)


class BankDoesNotHaveEnough(BankerExceptions):

    def __init__(self, msg: str, chips_available: int, chips_needed: int):
        self.msg = msg
        self.chips_available = chips_available,
        self.chips_needed = chips_needed
        super().__init__(msg)


class Banker:
    """
    The Banker's single responsibility is to exchange chips for other chips.
    """

    def __init__(
            self,
            chips: typing.List[game_tokens.Chip]
    ):
        self.chips = chips

    def exchange_chips(self, tray: typing.List[game_tokens.Chip], requesting: game_tokens.Chip):
        """
        Exchanges one set of chips for another set of equal value.

        :param tray: tray represents a physical container which is passed between the banker and a requestor.
            The contents of the tray are replaced with an equal value of the chips requested.
        :param requesting: The desired chips to be returned
        :return: typing.List[game_tokens.Chip]
        """
        # how much did they give you?
        total_value = sum(chip.value for chip in tray)

        # how much do they need back?
        chips_needed, remaining = divmod(total_value, requesting.value)
        if remaining:
            raise NotExactChange(
                f"Cannot make exact change with the tray provided!",
                chips_needed=chips_needed,
                remaining=remaining
            )

        # Do you have what they need?
        chips_available = self.chips.count(requesting)
        if chips_available < chips_needed:
            raise BankDoesNotHaveEnough(
                f"Not enough Chips are available in the bank to make the exchange!",
                chips_available=chips_available,
                chips_needed=chips_needed
            )

        # Take their chips
        while tray:
            self.chips.append(tray.pop())

        # Give them chips
        for chip in range(chips_needed):
            tray.append(self.chips.pop(self.chips.index(requesting)))


fives = [game_tokens.Chip(value=5, color="white") for i in range(10)]
twentyfives = [game_tokens.Chip(value=25, color="white") for j in range(10)]

test_chips = fives + twentyfives

b = Banker(chips=test_chips)

my_tray = [game_tokens.Chip(value=-1, color="white")]

b.exchange_chips(tray=my_tray, requesting=game_tokens.Chip(value=25, color="white"))
pass