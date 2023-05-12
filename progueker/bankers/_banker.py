import abc

from progueker.game_tokens import Chip


class Banker(abc.ABC):
    """
    The Banker's single responsibility is to distribute chips.
    """

    @abc.abstractmethod
    def exchange_chips(self, tray: list[Chip], requesting: Chip) -> None:
        """
        Exchanges one set of chips for another set of equal value. Must be exact change.

        :param tray: tray represents a physical container which is passed between the banker and a requestor.
            The contents of the tray are replaced with an equal value of the chips requested.
        :param requesting: The desired chips to be returned
        """
        pass

    @abc.abstractmethod
    def check_chip(self, chip: Chip) -> None:
        """
        Validates the authenticity of a chip.
        """

    @abc.abstractmethod
    def fill_tray(self, tray: list[Chip], chip: Chip, nchips: int) -> None:
        """
        Given a tray, fill it with the requested chips.
        """