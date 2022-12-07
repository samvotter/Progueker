import typing
import dataclasses


from progueker.interfaces.cmd_line.text_image_base import TextImage
from progueker.utils import EnumDict


@dataclasses.dataclass
class Banner(TextImage):

    """
    A Banner produces a center aligned bar-wrapped msg. IE:
    ===========
       hello
    ===========
    """

    msg: str
    pad: str = " "
    bar: str = "="

    def generate_image(
            self,
            resolution: typing.Tuple[int, int]
    ) -> str:
        width, height = resolution
        title = "\n".join(self.center_align(width=width, text=self.msg, pad=self.pad))
        return f"{self.bar * width}\n{title}\n{self.bar * width}\n"


@dataclasses.dataclass
class Box(TextImage):

    """
    A Box produces a left aligned str ringed by a bar symbol. IE:
    *********
    *hello  *
    *********
    """

    msg: str
    pad: str = " "
    bar: str = " "

    def generate_image(self, resolution: typing.Tuple[int, int]) -> str:
        width, height = resolution
        solid_bar = f"{self.bar * width}"
        text = "\n".join(f"{self.bar + line + self.bar}" for line in self.left_align(width=width - 2, text=self.msg))
        return f"{solid_bar}\n{text}\n{solid_bar}\n"


class CommonBanners(EnumDict):
    TITLE = Banner(msg="PrOgueKER")