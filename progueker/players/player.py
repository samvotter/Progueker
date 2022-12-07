import typing
import dataclasses

from progueker.game_tokens.cards import Card
from progueker.game_tokens.chips import Chip


@dataclasses.dataclass
class Player:
    name: str

    chips: typing.List[Chip] = dataclasses.field(default_factory=list)
    hand: typing.List[Card] = dataclasses.field(default_factory=list)
