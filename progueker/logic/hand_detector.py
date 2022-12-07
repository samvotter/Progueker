import typing
import itertools

from progueker.game_tokens.cards import Card
from progueker.utils import EnumDict


class HandHierarchy(EnumDict):
    HIGH_CARD       = 1
    TWO_OF_A_KIND   = 2
    TWO_PAIR        = 3
    THREE_OF_A_KIND = 4
    STRAIGHT        = 5
    FLUSH           = 6
    FULL_HOUSE      = 7
    FOUR_OF_A_KIND  = 8
    STRAIGHT_FLUSH  = 9


class HandDetector:

    def find_pairs(self, hand: typing.List[Card]) -> typing.Dict:
        """
        Returns a dictionary sorting cards with equal values. For example, given these cards:
            2 of Hearts
            3 of Hearts
            4 of Hearts
            3 of Clubs
            4 of Clubs
            4 of Diamonds
            11 of Spades

        We would expect to return:
            {
                2: [2 of Hearts],
                3: [3 of Hearts, 3 of Clubs],
                4: [4 of Hearts, 4 of Clubs, 4 of Diamonds],
                11: [11 of Spades]
            }

        Where the keys are the card value and the values are the cards in the pairs.

        :param hand: a list of card objects
        :return: a dictionary of pairs
        """
        hand = sorted(hand, key=lambda x: x.value)
        return {
            key: list(group) for key, group in itertools.groupby(hand, lambda x: x.value)
        }

    def find_sequences(self, hand: typing.List[Card]) -> typing.Dict:
        """
        Returns a dictionary sorting cards into sequences. For example, given these cards:
            2 of Hearts
            3 of Hearts
            4 of Hearts
            3 of Clubs
            4 of Clubs
            4 of Diamonds
            11 of Spades

        We would expect to return:
            {
                (2, 3, 4): {
                    2: [2 of Hearts],
                    3: [3 of Hearts, 3 of Clubs],
                    4: [4 of Hearts, 4 of Clubs, 4 of Diamonds]
                }
                (11,): {
                    11: [11 of Spades]
                }
            }

        :param hand: a list of card objects
        :return: a dictionary of {(straight_values): {straight_value: [Card., ...]}}
        """
        ret_dict = {}
        pair_dict = self.find_pairs(hand)
        unique_card_values = sorted(list(set(card.value for card in hand)))
        for key, group in itertools.groupby(enumerate(unique_card_values), lambda ix: ix[0] - ix[1]):
            sequential_card_values = tuple(ig[1] for ig in group)
            ret_dict[sequential_card_values] = {}
            for sequential_card_value in sequential_card_values:
                ret_dict[sequential_card_values][sequential_card_value] = pair_dict[sequential_card_value]
        return ret_dict

    def find_suits(self, hand: typing.List[Card]):
        """
        Returns a dictionary sorting cards into suits. For example, given these cards:
            2 of Hearts
            3 of Hearts
            4 of Hearts
            3 of Clubs
            4 of Clubs
            4 of Diamonds
            11 of Spades

        We would expect to return:
            {
                Hearts: [2 of Hearts, 3 of Hearts, 4 of Hearts],
                Clubs: [3 of Clubs, 4 of Clubs, 4 of Diamonds],
                Diamonds: [4 of Diamonds],
                Spades: [11 of Spades]
            }

        :param hand: a list of card objects
        :return: a dictionary of {suit_name: [Card, ...]}
        """
        hand = sorted(hand, key=lambda x: x.suit.name)
        return {
            key: list(group) for key, group in itertools.groupby(hand, lambda x: x.suit.name)
        }
