import abc
import typing


class Interface(abc.ABC):
    """
    The Interfaces's single responsibility is to present a mode of interaction for the application user.
    """

    def __init__(self, resolution: typing.Tuple[int, int]):
        self.width = resolution[0]
        self.height = resolution[1]


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






