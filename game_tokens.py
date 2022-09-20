import dataclasses
import typing


@dataclasses.dataclass(order=True)
class Chip:
    """
    A Chip's single responsibility is to represent money. Chips may come in any denomination and chips can be exchanged
    for other chips, but chips themselves are indivisible.
    """
    value: int
    color: str


@dataclasses.dataclass(frozen=True, order=True)
class DealerToken:
    """
    A Dealer Token's single responsibility is to represent who should be treated as the dealer.
    """
    pass


class Pot:
    """
    A Pot's single responsibility is to act as a repository for bids.
    """

    def __init__(self, chips: typing.List[Chip] = None):
        self.chips = chips
