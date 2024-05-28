"""
This module provides functionality to create a configuration object from parsed command-line arguments.

This module defines a function that converts parsed command-line arguments into a SimpleNamespace configuration
object. The configuration object contains all necessary parameters derived from the command-line arguments.
"""

from argparse import Namespace
from types import SimpleNamespace


def create_configuration_from_arguments(args: Namespace) -> SimpleNamespace:
    """
    Create and returns a configuration object from the provided command-line arguments.

    This function takes a Namespace object containing parsed command-line arguments and converts it into a
    SimpleNamespace configuration object. The configuration object includes parameters for verbose mode, debug
    mode, required parameters, and optional parameters.

    Arguments:
        args (Namespace): The parsed command-line arguments.

    Returns:
        SimpleNamespace: The configuration object containing the parameters derived from the command-line arguments.
    """
    config: SimpleNamespace = SimpleNamespace()

    config.create = args.create
    config.reconstruct = args.reconstruct
    config.shares = args.shares
    config.threshold = args.threshold
    config.output = args.output
    config.shares_directory = args.shares_directory

    return config
