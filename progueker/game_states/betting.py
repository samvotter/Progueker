from progueker.game_states.state_base import State
import enum
import typing


class BettingActions(enum.Enum):
    FOLD = 0
    CHECK = 1
    CALL = 2
    RAISE = 3


class BidResponse(State):

    def __init__(self, bid_total: int, transitions: typing.Dict[int, State]):
        self.bid_total = bid_total
        super().__init__(transitions=transitions)

    def go_to_next_state(self, event: typing.Any):
        return self.transitions[event](self.bid_total)


class Raise(BidResponse):

    def __init__(self, bid_total: int):
        transitions = {
            BettingActions.CALL: Call,
            BettingActions.FOLD: Fold,
            BettingActions.RAISE: Raise
        }
        super().__init__(bid_total=bid_total, transitions=transitions)


class Call(State):

    def __init__(self, bid_total: int):
        self.bid_total = bid_total



