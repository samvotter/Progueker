import dataclasses


@dataclasses.dataclass(order=True)
class Chip:
    """
    A Chip's single responsibility is to represent money. Chips may come in any denomination and chips can be exchanged
    for other chips, but chips themselves are indivisible.
    """
    sort_index: int = dataclasses.field(init=False)
    value: int
    color: str

    def __post_init__(self):
        self.sort_index = self.value
