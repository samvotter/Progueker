import argparse
import importlib
import os


def determine_operating_system():
    return "Windows" if os.name in ["nt"] else "Linux"


def main(runtime_args: argparse.Namespace, runtime_os: str):
    print("Starting application . . .")
    imp_module = importlib.import_module(f"interfaces.{runtime_args.interface}")
    face_name = runtime_args.interface.split("_")
    face_name = "".join(token.capitalize() for token in face_name)
    face = getattr(imp_module, f"{face_name}{runtime_os}")
    runtime_interface = face()
    runtime_interface.generate_display()


if __name__ == "__main__":
    # determine operating system
    operating_system = determine_operating_system()
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
    main(args, operating_system)
