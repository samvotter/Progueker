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
    def center_align(width: int, text: str, pad: str = " ") -> str:
        text_size = len(text)
        if text_size > width:
            raise ValueError(f"Text is too big, it does not need to be center-aligned")
        padding_needed = width - text_size
        side, remainder = divmod(padding_needed, 2)
        return f"{pad * side}{pad * remainder}{text}{pad * side}\n"

    @staticmethod
    def str_wrap(width: int, text: str, wrap: str = "=") -> str:
        return f"{wrap * width}\n{text}{wrap * width}\n"
