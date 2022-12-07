import typing
import random

from progueker.players.player import Player
from progueker.game_tokens.cards import Card
from progueker.game_tokens.chips import Chip
from progueker.players.betting_signals import BettingSignals


class RandomAIPlayer(Player):

    def __init__(
            self,
            name: str,
            chips: typing.List[Chip] = None,
            hand: typing.List[Card] = None
    ):
        self.name = name
        self.chips = chips or []
        self.hand = hand or []

    def fold(self):
        return BettingSignals.FOLD





class RandomAIPlayer(AIPlayer):
    """
    A random AI player takes purely random actions.
    """

    def __init__(
            self,
            name: str,
            chips: typing.List[game_tokens.Chip] = None,
            hand: hands.Hand = None
    ):
        self._bid_behaviors = {
            BettingActions.CALL: self._call_bid,
            BettingActions.RAISE: self._raise_bid
        }
        super().__init__(name=name, chips=chips, hand=hand)

    def make_bid_choice(self, bid: typing.List[game_tokens.Chip]) -> BettingActions:
        options = list(BettingActions)
        if bid:
            options.remove(BettingActions.CHECK)
        selection = random.choice(options)
        if selection in [BettingActions.FOLD, BettingActions.CHECK]:
            return selection
        return self._bid_behaviors[selection](bid)

    def _call_bid(self, bid: typing.List[game_tokens.Chip]) -> BettingActions:
        ask = sum(chip.value for chip in bid)
        try:
            chips_needed = ChipLogic.determine_chips_needed_biggest_first(ask, self.chips)
            for chip in chips_needed:
                self.bid.append(self.chips.pop(self.chips.index(chip)))
        except RequestLargerThanAvailable as err:
            if err.alloc:
                # we have enough chips to call the bid, but not the correct distribution of values. We must raise
                for chip in err.alloc:
                    self.bid.append(self.chips.pop(self.chips.index(chip)))
                return self._random_raise(ask)
            self._all_in()
        return BettingActions.CALL

    def _raise_bid(self, bid: typing.List[game_tokens.Chip]) -> BettingActions:
        ask = sum(chip.value for chip in bid)
        available = sum(chip.value for chip in self.chips)
        if ask > available:
            self._all_in()
            return BettingActions.CALL
        return self._random_raise(ask)

    def _random_raise(self, ask: int) -> BettingActions:
        while sum(chip.value for chip in self.bid) < ask:
            self.bid.append(self.chips.pop(self.chips.index(random.choice(self.chips))))
        return BettingActions.RAISE


class ChipLogicExceptions(Exception):
    pass


class RequestLargerThanAvailable(ChipLogicExceptions):

    def __init__(self, req, ava, alloc):
        self.req = req
        self.ava = ava
        self.alloc = alloc

    def __str__(self):
        return f"Cannot satisfy the requested amount.\n" \
               f"\tRequested: {self.req}\n" \
               f"\tAvailable: {self.ava}\n" \
               f"\tAlready Allocated: {self.alloc}"


class ChipLogic:
    """
    ChipLogic's single responsibility is to automatically satisfy Chip behavior requirements.
    """

    @classmethod
    def determine_chips_needed_biggest_first(
            cls,
            requested_amount: int,
            available: typing.List[game_tokens.Chip],
            allocated: typing.List[game_tokens.Chip] = None
    ) -> typing.List[game_tokens.Chip]:
        """
        This recursive algorithm for determining how to match a given value with a given collection of chips attempts
            to use the greatest amount of the largest chips first.

        It is not guaranteed to find a solution even if a solution exists, however it should work in the vast majority
        of cases.

        :param requested_amount: The amount we need to find given the chips available
        :param available: The collection of chips we can select from to create the requested amount
        :param allocated: The chips already selected from the available collection
        :return: List of chips equal to the requested amount.
        """
        allocated = allocated or []
        if requested_amount == 0:
            return allocated
        # do we have enough to satisfy the requested amount
        if sum(thing.value for thing in available) < requested_amount:
            raise RequestLargerThanAvailable(requested_amount, available, allocated)

        # what is the biggest token?
        available = list(sorted(available, key=lambda x: x.value))
        biggest_token = max(available, key=lambda x: x.value)

        # is that too big?
        if biggest_token.value > requested_amount:
            return cls.determine_chips_needed_biggest_first(
                requested_amount,
                available[:available.index(biggest_token)],
                allocated
            )

        # how many of the biggest token do I have?
        biggest_tokens = available[available.index(biggest_token):]

        # how many of the biggest token should I give?
        should_give, remaining = divmod(requested_amount, biggest_token.value)
        will_give = min(should_give, len(biggest_tokens))

        # adjust values
        allocated.extend([available.pop(available.index(biggest_token)) for _ in range(will_give)])
        requested_amount -= will_give * biggest_token.value
        return cls.determine_chips_needed_biggest_first(requested_amount, available, allocated)


ones = [game_tokens.Chip(value=1, color="white") for _ in range(40)]
fives = [game_tokens.Chip(value=5, color="blue") for _ in range(40)]
tens = [game_tokens.Chip(value=10, color="red") for _ in range(40)]
twentyfives = [game_tokens.Chip(value=25, color="yellow") for _ in range(40)]

test_chips = ones + fives + tens + twentyfives

random_ai = RandomAIPlayer(name="Test Player", chips=test_chips)
test_banker = actors.Banker()

for _ in range(20):
    test_bid = [game_tokens.Chip(value=random.randint(1, 10), color="test_color") for _ in range(10)]
    bid_value = sum(chip.value for chip in test_bid)
    print(f"Start of Bid:\n"
          f"\tChips: {sum(chip.value for chip in random_ai.chips)}\n")
    print(f"Bid: {bid_value}")
    result = random_ai.make_bid_choice(test_bid)
    print(f"End of Bid:\n"
          f"\tAction: {result}\n"
          f"\tBid: {sum(chip.value for chip in random_ai.bid)}\n")
    test_banker.take_chips(random_ai.bid)
