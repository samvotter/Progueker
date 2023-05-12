from progueker.game_tokens._cards._card import Card
from progueker.game_tokens._cards._suit import Suit


def test_card_compare_value():
    one = Card(value=1, suit=Suit(0, "test", "test"), name="test")
    two = Card(value=2, suit=Suit(0, "test", "test"), name="test")
    assert two > one


def test_card_compare_suit():
    one = Card(value=1, suit=Suit(0, "test", "test"), name="test")
    two = Card(value=1, suit=Suit(1, "test", "test"), name="test")
    assert two > one
