import pytest

from progueker.logic.hand_detector import HandDetector
from progueker.game_tokens.cards import StandardSuits, Card


@pytest.mark.parametrize(
    "cards, expected_pairs", [
        (
                [
                    Card(StandardSuits.HEARTS, 1, "one"),
                    Card(StandardSuits.CLUBS, 2, "two"),
                    Card(StandardSuits.DIAMONDS, 2, "two"),
                    Card(StandardSuits.SPADES, 3, "three"),
                    Card(StandardSuits.HEARTS, 3, "three"),
                    Card(StandardSuits.CLUBS, 3, "three")
                ],
                {
                    1: [
                        Card(StandardSuits.HEARTS, 1, "one")
                    ],
                    2: [
                        Card(StandardSuits.CLUBS, 2, "two"),
                        Card(StandardSuits.DIAMONDS, 2, "two")
                    ],
                    3: [
                        Card(StandardSuits.SPADES, 3, "three"),
                        Card(StandardSuits.HEARTS, 3, "three"),
                        Card(StandardSuits.CLUBS, 3, "three")
                    ]
                }
        ),
        (
                [
                    Card(StandardSuits.HEARTS, 3, "three"),
                    Card(StandardSuits.CLUBS, 8, "eight"),
                    Card(StandardSuits.DIAMONDS, 3, "three"),
                    Card(StandardSuits.SPADES, 3, "three")
                ],
                {
                    3: [
                        Card(StandardSuits.HEARTS, 3, "three"),
                        Card(StandardSuits.DIAMONDS, 3, "three"),
                        Card(StandardSuits.SPADES, 3, "three")
                    ],
                    8: [
                        Card(StandardSuits.CLUBS, 8, "eight")
                    ],
                }
        ),
        (
                [
                    Card(StandardSuits.HEARTS, 3, "three"),
                    Card(StandardSuits.CLUBS, 8, "eight"),
                    Card(StandardSuits.DIAMONDS, 3, "three"),
                    Card(StandardSuits.SPADES, 8, "eight"),
                    Card(StandardSuits.HEARTS, 3, "three")
                ],
                {
                    3: [
                        Card(StandardSuits.HEARTS, 3, "three"),
                        Card(StandardSuits.DIAMONDS, 3, "three"),
                        Card(StandardSuits.HEARTS, 3, "three")
                    ],
                    8: [
                        Card(StandardSuits.CLUBS, 8, "eight"),
                        Card(StandardSuits.SPADES, 8, "eight")
                    ],
                }
        ),
        (
                [
                    Card(StandardSuits.HEARTS, 2, "Two"),
                    Card(StandardSuits.HEARTS, 3, "Three"),
                    Card(StandardSuits.HEARTS, 4, "Four"),
                    Card(StandardSuits.CLUBS, 3, "Three"),
                    Card(StandardSuits.CLUBS, 4, "Four"),
                    Card(StandardSuits.DIAMONDS, 4, "Four"),
                    Card(StandardSuits.SPADES, 11, "Eleven")
                ],
                {
                    2: [
                        Card(StandardSuits.HEARTS, 2, "Two")
                    ],
                    3: [
                        Card(StandardSuits.HEARTS, 3, "Three"),
                        Card(StandardSuits.CLUBS, 3, "Three")
                    ],
                    4: [
                        Card(StandardSuits.HEARTS, 4, "Four"),
                        Card(StandardSuits.CLUBS, 4, "Four"),
                        Card(StandardSuits.DIAMONDS, 4, "Four")
                    ],
                    11: [
                        Card(StandardSuits.SPADES, 11, "Eleven")
                    ]
                }
        ),
    ]
)
def test_find_pairs(cards, expected_pairs):
    pairs = HandDetector().find_pairs(cards)
    assert pairs == expected_pairs


@pytest.mark.parametrize(
    "cards, expected_sequences", [
        (
                [
                    Card(StandardSuits.HEARTS, 2, "Two"),
                    Card(StandardSuits.HEARTS, 3, "Three"),
                    Card(StandardSuits.HEARTS, 4, "Four"),
                    Card(StandardSuits.CLUBS, 3, "Three"),
                    Card(StandardSuits.CLUBS, 4, "Four"),
                    Card(StandardSuits.DIAMONDS, 4, "Four"),
                    Card(StandardSuits.SPADES, 11, "Eleven")
                ],
                {
                    (2, 3, 4): {
                        2: [
                            Card(StandardSuits.HEARTS, 2, "Two")
                        ],
                        3: [
                            Card(StandardSuits.HEARTS, 3, "Three"),
                            Card(StandardSuits.CLUBS, 3, "Three")
                        ],
                        4: [
                            Card(StandardSuits.HEARTS, 4, "Four"),
                            Card(StandardSuits.CLUBS, 4, "Four"),
                            Card(StandardSuits.DIAMONDS, 4, "Four")
                        ]
                    },
                    (11,): {
                        11: [
                            Card(StandardSuits.SPADES, 11, "Eleven")
                        ]
                    }
                }
        )
    ]
)
def test_find_sequences(cards, expected_sequences):
    sequences = HandDetector().find_sequences(cards)
    assert sequences == expected_sequences


