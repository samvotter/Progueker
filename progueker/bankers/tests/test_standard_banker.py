import pytest

from progueker.bankers._standard_banker import StandardBanker
from progueker.game_tokens import Chip, NoSuchChipException


def test_fill_tray_empties_contents():
    original_chip = Chip(value=7, color="blue")
    requesting = Chip(value=10, color="green")
    tray = [original_chip]
    banker = StandardBanker({requesting})

    banker.fill_tray(tray, requesting, 1)

    assert original_chip not in tray


def test_fill_tray_replaces_contents():
    original_chip = Chip(value=7, color="blue")
    requesting = Chip(value=10, color="green")
    tray = [original_chip]
    banker = StandardBanker({requesting})

    banker.fill_tray(tray, requesting, 1)

    assert tray == [requesting]


def test_check_chip_does_not_raise_if_is_chip():
    original_chip = Chip(value=7, color="blue")
    banker = StandardBanker({original_chip})
    banker.check_chip(original_chip)


def test_check_chip_raises_if_no_chip():
    original_chip = Chip(value=7, color="blue")
    banker = StandardBanker()
    with pytest.raises(NoSuchChipException):
        banker.check_chip(original_chip)

