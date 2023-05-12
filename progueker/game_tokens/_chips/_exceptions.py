from ._chips import Chip


class ChipException(Exception):
    pass


class NoSuchChipException(ChipException):

    def __init__(self, chip: Chip):
        self.chip = chip

    def __str__(self):
        return f"{self.chip} does not exist!"
