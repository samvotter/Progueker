import abc
import typing
import dataclasses

from progueker.interfaces.cmd_line.text_image_base import TextImage


class Option(TextImage):

    """
    An options single responsibility is to represent a possible selectable action to the application user
    """

    @abc.abstractmethod
    def get_matching_symbol(self) -> str:
        """
        The str input a user provides to signify this option
        """
        pass


@dataclasses.dataclass
class StandardOption(Option):

    name: str
    matching_symbol: str

    def generate_image(self, resolution: typing.Tuple[int, int]) -> str:
        return f"{self.name}: <{self.get_matching_symbol()}>"

    def get_matching_symbol(self) -> str:
        return self.matching_symbol


class OptionMenu(list):

    """
    An OptionMenu's single responsibility is to represent a collection of possible actions to the application user
    """

    def __init__(self, options: typing.List[Option]):
        super().__init__(options)

    def get_options_str(self, resolution: typing.Tuple[int, int]) -> str:
        for idx, option in enumerate(self):
            yield f"{idx}. {option.generate_image(resolution)}>\n"

    def get_matching_symbols(self) -> set:
        option_symbols = set(option.get_matching_symbol() for option in self)
        if len(option_symbols) < len(self):
            raise ValueError(f"Options contain duplicate matching symbols. {self}")
        return option_symbols

