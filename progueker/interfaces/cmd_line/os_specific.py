import typing
import abc
import os


class OSMethods(abc.ABC):
    """
    OSMethods' single responsibility is to encapsulate os specific implementations.
    """

    @staticmethod
    @abc.abstractmethod
    def resize(resolution: typing.Tuple[int, int]):
        """
        Change resolution
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def clear_screen():
        """
        Reset interface to clean slate
        """
        pass


class OSMethodsWindows(OSMethods):
    """
    Supplies Windows Specific method implementations
    """

    @staticmethod
    def resize(resolution: typing.Tuple[int, int]):
        width, height = resolution
        os.system(f'mode con: cols={width} lines={height}')

    @staticmethod
    def clear_screen():
        os.system("cls")


class OSMethodsLinux(OSMethods):
    """
    Supplies Linux Specific method implementations
    """

    @staticmethod
    def resize(resolution: typing.Tuple[int, int]):
        # TODO implement this
        raise NotImplemented("Resizing the screen for linux has not yet been implemented.")

    @staticmethod
    def clear_screen():
        os.system("clear")
