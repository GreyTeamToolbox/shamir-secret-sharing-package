"""
This module provides command-line argument parsing, processing, and execution functionalities for the application.

This module defines the main functions for setting up the argument parser, processing the arguments, and running the
main logic of the application. The module uses the argparse library to handle command-line arguments and the wolfsoftware.drawlines
module to draw lines for output formatting. It also utilizes the config module to create configurations from the parsed arguments.
"""

import argparse
import sys

from types import SimpleNamespace

from wolfsoftware.notify import error_message

from .config import create_configuration_from_arguments
from .create import create_shares
from .globals import ARG_PARSER_DESCRIPTION, ARG_PARSER_EPILOG, ARG_PARSER_PROG_NAME, VERSION_STRING
from .reconstruct import reconstruct_shares


def setup_arg_parser() -> argparse.ArgumentParser:
    """
    Set up and returns the argument parser with all required flags, optional, and required arguments.

    This function creates an ArgumentParser object and defines the available command-line arguments, including flags for help,
    debug, verbose, and version information. It also sets up optional and required argument groups for additional parameters.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    parser = argparse.ArgumentParser(prog=ARG_PARSER_PROG_NAME,
                                     add_help=False,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description=ARG_PARSER_DESCRIPTION,
                                     epilog=ARG_PARSER_EPILOG)

    flags: argparse._ArgumentGroup = parser.add_argument_group(title='flags')
    optional: argparse._ArgumentGroup = parser.add_argument_group(title='optional')
    required: argparse._ArgumentGroup = parser.add_argument_group(title='required')
    mutex_group: argparse._MutuallyExclusiveGroup = required.add_mutually_exclusive_group(required=True)

    flags.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS, help="Show this help message and exit")
    flags.add_argument('-V', '--version', action="version", version=VERSION_STRING, help="Show program's version number and exit.")

    optional.add_argument('-s', '--shares', type=int, help='Total number of shares to create')
    optional.add_argument('-t', '--threshold', type=int, help='Threshold number of shares needed to reconstruct the secret')
    optional.add_argument('-o', '--output', action='store_true', help='Output shares to screen instead of writing to files')
    optional.add_argument('-d', '--shares-directory', type=str, default='shares', help='Where to write the shares files.')

    mutex_group.add_argument('-c', '--create', type=str, help='The secret to share or the file containing the secret')
    mutex_group.add_argument('-r', '--reconstruct', nargs='+', metavar='SHARE', help='List of shares in the form "x,y" or file paths ending with .txt')

    return parser


def process_arguments(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """
    Process and validates the command-line arguments.

    This function uses the provided argument parser to parse the command-line arguments. It validates the parsed arguments
    and returns them in a Namespace object.

    Args:
        parser (argparse.ArgumentParser): The argument parser to use for parsing the command-line arguments.

    Returns:
        argparse.Namespace: The parsed and validated arguments.
    """
    args: argparse.Namespace = parser.parse_args()

    if args.create and args.shares and args.threshold:
        if args.shares <= 1 or args.threshold <= 1:
            print(error_message("Total number of shares and threshold must be greater than 1"))
            sys.exit(1)
        if args.threshold > args.shares:
            print(error_message("Threshold must be less than or equal to the total number of shares"))
            sys.exit(0)

    return args


def run() -> None:
    """
    Master controller function.

    This function sets up the argument parser, processes the command-line arguments, creates the configuration from
    the arguments, and executes the main functionality. It handles errors related to argument parsing and exits with
    an appropriate status code in case of failure.
    """
    parser: argparse.ArgumentParser = setup_arg_parser()
    try:
        args: argparse.Namespace = process_arguments(parser)
        config: SimpleNamespace = create_configuration_from_arguments(args)
        if config.create:
            create_shares(config)
        else:
            reconstruct_shares(config)
    except argparse.ArgumentTypeError as err:
        parser.print_usage()
        print(err)
        sys.exit(1)
