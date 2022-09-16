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


class BankerExceptions(Exception):
    pass

class NotExactChange(BankerExceptions):
    pass

class BankDoesNotHaveEnough(BankerExceptions):

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
                f"The tray does not contain enough chips to perform the exchange\n"
                f"\tValue Provided: {total_value}\n"
                f"\tChips Needed:   {chips_needed} * {requesting.value} = {chips_needed * requesting.value}\n"
                f"\tRemainder:      {remaining}"
            )

        # Do you have what they need?
        chips_available = self.chips.count(requesting)
        if chips_available >= chips_needed:
            while tray:
                self.chips.append(tray.pop())
            for chip in range(chips_needed):
                tray.append(self.chips.pop(self.chips.index(requesting)))
        raise BankDoesNotHaveEnough(
            f"Not enough Chips are available in the bank to make the exchange!\n"
            f"\tAvailable: {chips_available}\n"
            f"\tNeeded:    {chips_needed}"
        )