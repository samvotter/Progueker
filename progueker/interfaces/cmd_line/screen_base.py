import typing
import dataclasses
import os

from progueker.interfaces.cmd_line.text_image_base import TextImage
from progueker.interfaces.cmd_line.option_base import Option
from progueker.interfaces.cmd_line.os_specific import OSMethodsWindows, OSMethodsLinux

OS_METHODS = OSMethodsLinux
if os.name == "nt":
    OS_METHODS = OSMethodsWindows


class AskForInput(TextImage):

    def generate_image(self, resolution: typing.Tuple[int, int]) -> str:
        width, height = resolution
        return self.left_align(width=width, text="Please select an action:")


@dataclasses.dataclass
class Screen:

    """
    A Screen's single responsibility is to display some image and then solicit the user for a response which then
    provided to the game server.
    """
    images: typing.List[TextImage] = dataclasses.field(default_factory=list)
    options: typing.Dict[str, Option] = dataclasses.field(default_factory=dict)

    _os: OS_METHODS = dataclasses.field(default=OS_METHODS, init=False)

    def _display_image(self, resolution: typing.Tuple[int, int]) -> None:
        self._os.clear_screen()
        for image in self.images:
            print(image.generate_image(resolution))
        for idx, option in enumerate(self.options.values()):
            print(f"{idx + 1}. {option.generate_image(resolution)}")

    @staticmethod
    def _ask_for_input(resolution: typing.Tuple[int, int]) -> str:
        return input("".join(line for line in AskForInput().generate_image(resolution)) + "\n")

    def display_ask(self, resolution: typing.Tuple[int, int]) -> str:
        self._display_image(resolution)
        return self._ask_for_input(resolution)

    def run(self, resolution: typing.Tuple[int, int]) -> Option:
        user_choice = self.display_ask(resolution)
        while user_choice not in [option.get_matching_symbol() for option in self.options.values()]:
            user_choice = self.display_ask(resolution)
        return self.options[user_choice]
