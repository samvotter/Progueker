import abc

import card_objects
import game_tokens
import random
import typing
import hands


class Player(abc.ABC):
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

    def _all_in(self):
        while self.chips:
            self.bid.append(self.chips.pop())

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

    def __init__(self, requested_amount: int, chip_value: int):
        self.requested = requested_amount
        self.chip_value = chip_value

    def __str__(self):
        return f"Cannot make exact change with the tray provided!\n" \
               f"\tThe given amount: {self.requested} is not divisible by: {self.chip_value}\n"


class BankDoesNotHaveEnough(BankerExceptions):

    def __init__(self, chips_available: int, chips_needed: int):
        self.chips_available = chips_available,
        self.chips_needed = chips_needed

    def __str__(self):
        return f"Not enough Chips are available in the bank to make the exchange!\n" \
               f"\tChips Needed: {self.chips_needed}\n" \
               f"\tChips Available: {self.chips_available}\n"


class Banker:
    """
    The Banker's single responsibility is to manage interactions with chips outside of player counts.
    """

    def __init__(
            self,
            chips: typing.List[game_tokens.Chip] = None
    ):
        self.chips = chips or []

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
            raise NotExactChange(requested_amount=total_value, chip_value=requesting.value)

        # Do you have what they need?
        chips_available = self.chips.count(requesting)
        if chips_available < chips_needed:
            raise BankDoesNotHaveEnough(chips_available=chips_available, chips_needed=chips_needed)

        # Take their chips
        self.take_chips(tray)

        # Give them chips
        for chip in range(chips_needed):
            tray.append(self.chips.pop(self.chips.index(requesting)))
