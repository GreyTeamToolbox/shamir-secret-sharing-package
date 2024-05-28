#!/usr/bin/env python
"""
This script serves as the entry point for the application.

This script initializes the application by invoking the main routine. It handles
command-line argument processing and ensures the application runs as intended.
The script also gracefully handles keyboard interrupts to allow for a clean exit.
"""

import sys

from wolfsoftware.notify import system_message

from .cli import run


def main() -> None:
    """
    Execute the main routine of the script.

    This function serves as the entry point of the script. It is responsible
    for invoking the `run` function, which handles the main functionality
    of the application. The `main` function does not take any parameters
    and does not return any value. It ensures that the script's functionality
    is triggered correctly when the script is executed.
    """
    try:
        run()
    except KeyboardInterrupt:
        print(system_message("\n[*] Exiting Program\n"))
        sys.exit(1)


if __name__ == "__main__":
    main()
