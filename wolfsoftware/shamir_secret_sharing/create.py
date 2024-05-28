"""
Functions for creating shares from a secret using Shamir's Secret Sharing.

This module provides functions to generate the actual shares from a secret and to create shares based on a given configuration.
"""

from types import SimpleNamespace
from typing import List, Tuple

from .constants import MAX_SECRET_LENGTH
from .maths import generate_coefficients, polynomial
from .utils import read_secret_from_file, write_shares_to_files, string_to_bytes, bytes_to_int


def create_actual_shares(secret: str, total_shares: int, threshold: int) -> list:
    """
    Create the actual shares from a given secret using Shamir's Secret Sharing.

    Arguments:
        secret (str): The secret to be shared.
        total_shares (int): The total number of shares to create.
        threshold (int): The minimum number of shares required to reconstruct the secret.

    Returns:
        list: A list of tuples, each containing a share index and its corresponding value.
    """
    secret_bytes: bytes = string_to_bytes(secret)
    secret_int: int = bytes_to_int(secret_bytes)

    # Check if the secret is too long for the fixed prime
    if len(secret_bytes) > MAX_SECRET_LENGTH:
        raise ValueError(f"Secret is too long. Maximum length is {MAX_SECRET_LENGTH} bytes.")

    coefficients: List = generate_coefficients(secret_int, threshold)
    shares: List[Tuple[int, int]] = [(i, polynomial(i, coefficients)) for i in range(1, total_shares + 1)]
    return shares


def create_shares(config: SimpleNamespace) -> None:
    """
    Create shares based on the given configuration and write them to files or print them to the output.

    Arguments:
        config (SimpleNamespace): The configuration containing the secret, number of shares, threshold,
                                  and output options.
    """
    if config.create.endswith('.txt'):
        secret: str = read_secret_from_file(config.create)
    else:
        secret = config.create

    shares: List = create_actual_shares(secret, config.shares, config.threshold)

    write_shares_to_files(shares, config.output, config.shares_directory)
