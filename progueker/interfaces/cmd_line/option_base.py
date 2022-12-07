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
        width, height = resolution
        return "".join(line for line in self.left_align(width=width, text=f"{self.name}: <{self.matching_symbol}>"))

    def get_matching_symbol(self) -> str:
        return self.matching_symbol
