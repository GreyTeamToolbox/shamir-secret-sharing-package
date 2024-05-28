"""
Functions for reconstructing a secret from shares using Shamir's Secret Sharing.

This module provides functions to reconstruct the original secret from given shares and a configuration.
"""

from types import SimpleNamespace

from typing import Any, List, Tuple

from .constants import FIXED_LARGE_PRIME
from .maths import lagrange_interpolation
from .utils import read_share_from_file, int_to_bytes, bytes_to_string


def reconstruct_secret(shares: list, prime: int) -> int:
    """
    Reconstruct the secret integer from the given shares using Lagrange interpolation.

    Arguments:
        shares (list): The list of shares, each a tuple containing the share index and value.
        prime (int): The prime number used in the sharing scheme.

    Returns:
        int: The reconstructed secret as an integer.
    """
    secret_int: int = lagrange_interpolation(0, shares, prime)
    return secret_int


def reconstruct_shares(config: SimpleNamespace) -> None:
    """
    Reconstruct the secret from the given shares based on the configuration and either print it or write it to a file.

    Arguments:
        config (SimpleNamespace): The configuration containing the list of share files and output options.
    """
    shares: List[Tuple] = [read_share_from_file(share_file) for share_file in config.reconstruct]

    prime: Any = FIXED_LARGE_PRIME

    # Calculate the maximum length of the shares
    max_share_value: Any = max(share[1] for share in shares)
    original_length: Any = (max_share_value.bit_length() + 7) // 8

    secret_int: int = reconstruct_secret(shares, prime)
    secret_bytes: bytes = int_to_bytes(secret_int, original_length)
    reconstructed_secret: str = bytes_to_string(secret_bytes)

    if config.output:
        print(f'Reconstructed secret: {reconstructed_secret}')
    else:
        with open('reconstructed-secret.txt', 'w', encoding='utf-8') as f:
            f.write(f"{reconstructed_secret}\n")
        print('Reconstructed secret written to reconstructed-secret.txt')
