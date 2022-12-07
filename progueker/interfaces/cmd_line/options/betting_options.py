
from progueker.utils import EnumDict
from progueker.interfaces.cmd_line.option_base import StandardOption


class BettingOptions(EnumDict):
    FOLD = StandardOption(name="Fold",      matching_symbol="f")
    CALL = StandardOption(name="Call",      matching_symbol="c")
    RAISE = StandardOption(name="Raise",    matching_symbol="r")
