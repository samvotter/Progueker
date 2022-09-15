import typing
import enum
import itertools
from card_objects import Card, Suit


class HandHierarchy(enum.IntEnum):
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







c1 = Card(suit=Suit(name="test1", color="testcol1"), value=1, name="one")
c2 = Card(suit=Suit(name="test2", color="testcol2"), value=2, name="two")
c4 = Card(suit=Suit(name="test1", color="testcol4"), value=4, name="four")
c5 = Card(suit=Suit(name="test2", color="testcol5"), value=5, name="five")
c6 = Card(suit=Suit(name="test1", color="testcol6"), value=6, name="six")
c7 = Card(suit=Suit(name="test2", color="testcol7"), value=7, name="seven")
c8 = Card(suit=Suit(name="test3", color="testcol8"), value=8, name="eight")
c9 = Card(suit=Suit(name="test4", color="testcol9"), value=1, name="one")
c10 = Card(suit=Suit(name="test1", color="testcol10"), value=2, name="two")
c11 = Card(suit=Suit(name="test2", color="testcol11"), value=4, name="four")
c12 = Card(suit=Suit(name="test3", color="testcol12"), value=5, name="five")
c13 = Card(suit=Suit(name="test4", color="testcol13"), value=6, name="six")
c14 = Card(suit=Suit(name="test5", color="testcol14"), value=7, name="seven")
c15 = Card(suit=Suit(name="test1", color="testcol15"), value=8, name="eight")
c16 = Card(suit=Suit(name="test1", color="testcol15"), value=12, name="eight")


hd = HandDetector()
straight_dict = hd.find_suits(hand=[c1, c2, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16])
pass
