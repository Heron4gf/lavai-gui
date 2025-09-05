import argparse
import sys
from .gui import main as gui_main


def main():
    """Main entry point for the lavai-gui command line interface."""
    parser = argparse.ArgumentParser(
        description="Lavai GUI - A graphical interface for managing AI provider credentials"
    )
    parser.add_argument(
        "command",
        choices=["start"],
        help="Command to execute. Use 'start' to launch the GUI."
    )
    
    # If no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    args = parser.parse_args()
    
    if args.command == "start":
        gui_main()


if __name__ == "__main__":
    main()
