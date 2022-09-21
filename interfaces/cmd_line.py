from interfaces.interface_base import Interface
import typing
import os
import sys


class CmdLine(Interface):
    """
    The CmdLine's single responsibility is to render the game through the command line.
    """

    def __init__(self, resolution: typing.Tuple[int, int] = None):
        width = 120                                     # This value is measured in characters
        height = 30                                     # This value is measured in newline characters
        if resolution is not None:
            width = resolution[0]
            height = resolution[1]
        super().__init__(resolution=(width, height))
        self._pad_symbol = " "

    def generate_display(self):
        self._clear_screen()

    def close(self):
        sys.exit(0)

    def resize(self, resolution: typing.Tuple[int, int]):
        raise OSError("The implementation of resizing the terminal / console window is OS specific")

    def _split_to_width(self, text: str) -> typing.List[str]:
        return [text[i:i + self.width] for i in range(0, len(text), self.width)]

    def _center_align(self, text: str) -> str:
        text_size = len(text)
        total_padding = self.width - text_size
        left_padding, remaining = divmod(total_padding, 2)
        right_padding = left_padding
        if remaining:
            right_padding += remaining
        return f"{self._pad_symbol * left_padding}{text}{self._pad_symbol * right_padding}"

    def _clear_screen(self):
        raise OSError("The implementation of clearing the terminal / console window is OS specific")


class CmdLineWindows(CmdLine):

    def _clear_screen(self):
        os.system("cls")

    def resize(self, resolution: typing.Tuple[int, int]):
        width, height = resolution
        os.system(f'mode con: cols={width} lines={height}')
        self.__init__(resolution=(width, height))


class CmdLineLinux(CmdLine):

    def _clear_screen(self):
        os.system("clear")

    def resize(self, resolution: typing.Tuple[int, int]):
        # TODO implement this
        raise NotImplemented("Resizing the screen for linux has not yet been implemented.")


