import abc
import typing


class Interface(abc.ABC):
    """
    The Interface's single responsibility is to present a mode of interaction for the application user.
    """

    def __init__(self, resolution: typing.Tuple[int, int]):
        self.width, self.height = resolution

    @abc.abstractmethod
    def generate_display(self):
        """
        Provides the initial blank canvas to work with.
        """
        pass

    @abc.abstractmethod
    def close(self):
        """
        Exits the program
        """
        pass

    def resize(self, resolution: typing.Tuple[int, int]):
        """
        Change resolution of interface display.
        :return:
        """
        pass









