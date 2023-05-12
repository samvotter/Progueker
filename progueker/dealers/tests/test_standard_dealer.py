import pytest

from progueker.dealers._standard_dealer import StandardDealer
from progueker.game_tokens import Card, StandardSuits, RanOutOfCardsException


def test_standard_dealer_has_standard_deck():
    dealer = StandardDealer()
    assert len(dealer.deck) == 52


def test_draws_from_deck():
    dealer = StandardDealer()
    dealer.draw_from_deck(dealer.deck)
    assert len(dealer.deck) == 51


def test_draw_raises_when_no_cards():
    dealer = StandardDealer()
    with pytest.raises(RanOutOfCardsException):
        while True:
            dealer.draw_from_deck(dealer.deck)


def test_collect_removes_cards():
    card = Card(suit=StandardSuits.HEARTS, value=2, name="two")
    hand = [card]
    StandardDealer().collect_cards(hand)
    assert hand == []


def test_collect_adds_cards():
    card = Card(suit=StandardSuits.HEARTS, value=2, name="two")
    hand = [card]
    dealer = StandardDealer()
    dealer.collect_cards(hand)
    assert len(dealer.deck) == 53

