import dataclasses


@dataclasses.dataclass(frozen=True, order=True)
class Chip:
    """
    A Chip's single responsibility is to represent money. Chips may come in any denomination and can be exchanged
    for other chips, but chips themselves are indivisible.
    """
    value: int
    color: str
