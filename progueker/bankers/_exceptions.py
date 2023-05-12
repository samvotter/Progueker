class BankerExceptions(Exception):
    pass


class NotExactChangeException(BankerExceptions):

    def __init__(self, requested_amount: int, chip_value: int):
        self.requested = requested_amount
        self.chip_value = chip_value

    def __str__(self):
        return f"Cannot make exact change with the tray provided!\n" \
               f"\tThe given amount: {self.requested} is not divisible by: {self.chip_value}\n"


class BankDoesNotHaveEnoughException(BankerExceptions):

    def __init__(self, chips_available: int, chips_needed: int):
        self.chips_available = chips_available,
        self.chips_needed = chips_needed

    def __str__(self):
        return f"Not enough Chips are available in the bank to make the exchange!\n" \
               f"\tChips Needed: {self.chips_needed}\n" \
               f"\tChips Available: {self.chips_available}\n"