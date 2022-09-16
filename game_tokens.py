import dataclasses


@dataclasses.dataclass
class Chip:
    """
    A Chip's single responsibility is to represent money. Chips may come in any denomination and chips can be exchanged
    for other chips, but chips themselves are indivisible.
    """
    value: int
    color: str
