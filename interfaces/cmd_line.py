import card_objects
from interfaces.base import Interface
from game_states.startup import PokerSetup
import typing
import os
import sys
import game_tokens
import actors
import copy


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

        command = 'clear'
        if os.name in ('nt', 'dos'):                    # If Machine is running on Windows, use cls
            command = 'cls'
        self.__os_specific_clear_cmd = command
        self._application_title = self._generate_application_title()
        self._divider_bar = self._generate_divider_bar()

    def generate_display(self):
        self._clear_screen()

    def close(self):
        sys.exit(0)

    def _clear_screen(self):
        os.system(self.__os_specific_clear_cmd)
        print(self._application_title)
        print(self._divider_bar)

    def _generate_application_title(self) -> str:
        text = "Progueker"
        padding = self.width - len(text)
        left_pad = " " * (padding // 2)
        right_pad = left_pad
        if len(text) % 2:
            right_pad += " "
        return left_pad + text + right_pad

    def _generate_divider_bar(self) -> str:
        return "=" * self.width

    def _get_number_of_players(self) -> int:
        self._clear_screen()
        return int(input("How many players?\t"))

    def _get_chips(self) -> typing.List[game_tokens.Chip]:
        chips = []
        display_chips = []
        more = True
        while more:
            self._clear_screen()
            print(
                "Players need chips to place bets.\n"
                "You will be asked to give a chip value and how many of that chip each player should have."
            )
            if chips:
                print(sorted(display_chips, key=lambda x: x.value))
            chip_value = int(input("Chip Value:\t"))
            per_player = int(input("How many should each player have:\t"))
            chip_color = input("What color is the chip:\t")
            chips.extend(game_tokens.Chip(value=chip_value, color=chip_color) for i in range(per_player))
            display_chips.append(game_tokens.Chip(value=chip_value, color=chip_color))
            add_more = input("Add more chips (y/n):\t").lower()
            if add_more not in ["y", "yes"]:
                more = False
        return chips

    def _get_cards(self) -> card_objects.Deck:
        return card_objects.StandardDeck()

    def setup_game(self) -> PokerSetup:
        num_players = self._get_number_of_players()
        chips = self._get_chips()
        deck = self._get_cards()
        return PokerSetup(
            players=[actors.Player(name=f"PlaceHolder_{i}", chips=copy.deepcopy(chips)) for i in range(num_players)],
            chips=chips,
            deck=deck
        )