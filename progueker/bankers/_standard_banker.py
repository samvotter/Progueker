from ._banker import Banker
from ._exceptions import NotExactChangeException
from progueker.game_tokens import Chip, NoSuchChipException


class StandardBanker(Banker):

    def __init__(
            self,
            chips: set[Chip] = None
    ):
        self.chips = chips or {}

    def exchange_chips(self, tray: list[Chip], requesting: Chip) -> None:
        """
        Exchanges one set of chips for another set of equal value.
        """
        self.check_chip(requesting)

        total_value = sum(chip.value for chip in tray)
        chips_needed, remaining = divmod(total_value, requesting.value)
        if remaining:
            raise NotExactChangeException(requested_amount=total_value, chip_value=requesting.value)

        self.fill_tray(tray, requesting, chips_needed)

    def check_chip(self, chip: Chip) -> None:
        if chip not in self.chips:
            raise NoSuchChipException(chip)

    def fill_tray(self, tray: list[Chip], chip: Chip, nchips: int) -> None:
        tray.clear()
        tray.extend([chip for _ in range(nchips)])
