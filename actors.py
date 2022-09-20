import card_objects
import game_tokens
import random
import typing
import hands


class Player:
    """
    The Player's single responsibility is to represent a player at the table.
    """
    def __init__(
            self,
            name: str,
            chips: typing.List[game_tokens.Chip] = None,
            hand: hands.Hand = None,
    ):
        self.name = name
        self.chips = chips or []
        self.hand = hand or []
        self.bid = []

    def __str__(self):
        return f"{self.name}:\n" \
               f"\tChips: {sum(chip.value for chip in self.chips)}"


class DealerExceptions(Exception):
    pass


class RanOutOfCards(DealerExceptions):
    pass


class Dealer:
    """
    The Dealer's single responsibility is to deal cards.
    """

    def __init__(
            self,
            deck: card_objects.Deck,
    ):
        self.deck = deck

    def shuffle(self, cards: typing.List[card_objects.Card] = None) -> None:
        if cards is None:
            cards = self.deck
        random.shuffle(cards)

    def draw_from_deck(self, deck: card_objects.Deck = None) -> card_objects.Card:
        if deck is None:
            deck = self.deck
        if deck:
            return deck.stack.pop()
        raise RanOutOfCards(f"Cannot draw from deck, there are no more cards.")

    def deal_hands(self, hands_to_be_dealt: typing.List[hands.Hand], deck: card_objects.Deck = None) -> None:
        """
        :param hands_to_be_dealt: A list of cards. Only hands which need to be dealt more cards should ever be passed
        into this function. If a hand does not need to be dealt cards, it does not belong in a list called:
            "hands to be dealt"
        :param deck: Where the cards being dealt are coming from.
        :return: None. Modifies the state of the passed in hands of cards.
        """
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
    The Banker's single responsibility is to manage interactions with the chip supply.
    """

    def __init__(
            self,
            chips: typing.List[game_tokens.Chip]
    ):
        self.chips = chips

    def take_chips(self, tray: typing.List[game_tokens.Chip]) -> None:
        """
        Incorporate a tray of chips into the chip supply.

        :param tray: tray represents a physical container which is passed between the banker and a requestor.
            The contents of the tray are replaced with an equal value of the chips requested.
        :return: None, modifies the contents of the passed in tray
        """
        while tray:
            self.chips.append(tray.pop())

    def exchange_chips(self, tray: typing.List[game_tokens.Chip], requesting: game_tokens.Chip) -> None:
        """
        Exchanges one set of chips for another set of equal value. Must be exact change.

        :param tray: tray represents a physical container which is passed between the banker and a requestor.
            The contents of the tray are replaced with an equal value of the chips requested.
        :param requesting: The desired chips to be returned
        :return: None, modifies the contents of the passed in tray
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
        self.take_chips(tray)

        # Give them chips
        for chip in range(chips_needed):
            tray.append(self.chips.pop(self.chips.index(requesting)))
