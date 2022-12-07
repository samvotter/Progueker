import os


WIDTH, HEIGHT = (120, 30)
BAR = "="
TITLE = "PrOgueKER"
PAD = " "


def _center_align(width: int, text: str, pad: str = " ") -> str:
    text_size = len(text)
    if text_size > width:
        raise ValueError(f"Text is too big, it does not need to be center-aligned")
    padding_needed = width - text_size
    side, remainder = divmod(padding_needed, 2)
    return f"{pad * side}{pad * remainder}{text}{pad * side}\n"


def _bar_wrap(width: int, text: str, bar: str = "=") -> str:
    return f"{bar * width}\n{text}{bar * width}\n"


def _sanitize_inputs(text: str) -> str:
    text = text.lower()
    text = text.replace("<", "")
    text = text.replace(">", "")
    return text


def display_title() -> None:
    print(_bar_wrap(WIDTH, _center_align(WIDTH, TITLE, " "), "="))


OPTION_1 = "Start a New Game: <ng>"
OPTION_2 = "High Scores: <hs>"
OPTION_3 = "Close: <e>"


def display_options() -> None:
    print()
    print(OPTION_1)
    print(OPTION_2)
    print(OPTION_3)


def _clear_screen() -> None:
    os.system("cls")


def solicit_action() -> str:
    available_choices = ["ng", "hs", "e"]
    your_choice = _sanitize_inputs(input(f"Please select an option from: {available_choices}\n"))
    while your_choice not in ["ng", "hs", "e"]:
        _clear_screen()
        display_title()
        display_options()
        print()
        print(f"Did not recognise your choice: {your_choice}")
        your_choice = _sanitize_inputs(input(f"Please select an option from: {available_choices}\n"))
    return your_choice


_clear_screen()
display_title()
display_options()
solicit_action()
