import typing

from progueker.bankers.banker import Banker, BankerExceptions
from progueker.game_tokens.chips import Chip


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


class StandardBanker(Banker):

    def __init__(
            self,
            chips: typing.List[Chip] = None
    ):
        self.chips = chips or []

    def take_chips(self, tray: typing.List[Chip]) -> None:
        """
        Incorporate a tray of chips into the chip supply.

        :param tray: tray represents a physical container which is passed between the banker and a requestor.
            The contents of the tray are replaced with an equal value of the chips requested.
        :return: None, modifies the contents of the passed in tray
        """
        while tray:
            self.chips.append(tray.pop())

    def exchange_chips(self, tray: typing.List[Chip], requesting: Chip) -> None:
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
