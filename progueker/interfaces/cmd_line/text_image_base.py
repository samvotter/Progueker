import abc
import typing


class TextImage(abc.ABC):

    """
    A TextImage's single responsibility is to provide some sort of string representation of itself
    based on its current state and the available resolution of the display area
    """

    @abc.abstractmethod
    def generate_image(self, resolution: typing.Tuple[int, int]) -> str:
        """
        Returns an appropriately sized version of the image
        """
        pass

    @staticmethod
    def left_align(width: int, text: str, pad: str = " ") -> str:
        while len(text) > width:
            yield text[:width]
            text = text[width:]
        yield f"{text}{pad * (width - len(text))}"

    @staticmethod
    def center_align(width: int, text: str, pad: str = " ") -> str:
        while len(text) > width:
            yield text[:width]
            text = text[width:]
        padding_needed = width - len(text)
        side, remainder = divmod(padding_needed, 2)
        yield f"{pad * side}{pad * remainder}{text}{pad * side}"

    @staticmethod
    def right_align(width: int, text: str, pad: str = " ") -> str:
        while len(text) > width:
            yield text[:width]
            text = text[width:]
        yield f"{pad * (width - len(text))}{text}"

