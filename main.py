import argparse
import importlib


def main(runtime_args: argparse.Namespace):
    print("Starting application . . .")
    imp_module = importlib.import_module(f"interfaces.{runtime_args.interface}")
    face_name = runtime_args.interface.split("_")
    face_name = "".join(token.capitalize() for token in face_name)
    face = getattr(imp_module, face_name)
    runtime_interface = face()
    runtime_interface.generate_display()
    runtime_interface.setup_game()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Progueker is a Poker Roguelike. Thank you for playing!"
    )
    parser.add_argument(
        "-if", "--interface",
        type=str, default="cmd_line",
        help="Which interface would you like to use for the game?",
        required=True
    )
    args = parser.parse_args()
    main(args)