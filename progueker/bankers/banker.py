import abc
import typing

from progueker.game_tokens.chips import Chip


class BankerExceptions(Exception):
    pass


class Banker(abc.ABC):
    """
    The Banker's single responsibility is to manage interactions with chips outside of player counts.
    """

    @abc.abstractmethod
    def take_chips(self, tray: typing.List[Chip]) -> None:
        """
        Given some chips, take those chips.
        """
        pass

    @abc.abstractmethod
    def exchange_chips(self, tray: typing.List[Chip], requesting: Chip) -> None:
        """
        Exchanges one set of chips for another set of equal value. Must be exact change.

        :param tray: tray represents a physical container which is passed between the banker and a requestor.
            The contents of the tray are replaced with an equal value of the chips requested.
        :param requesting: The desired chips to be returned
        :return: None, modifies the contents of the passed in tray
        """
        pass
