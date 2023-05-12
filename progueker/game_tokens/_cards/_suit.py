import dataclasses


@dataclasses.dataclass(frozen=True, eq=True, order=True)
class Suit:
    """
    A suit's single responsibility is to identify a card as belonging to a set of other matching suits.
    """
    suit_order: int
    suit_name: str
    color: str

    def __str__(self):
        return self.suit_name
