"""
Utility functions for the wolfsoftware.shamir_secret_sharing package.

This module provides helper functions for converting between data types, reading secrets and shares from files,
and writing shares to files.
"""

import os
import sys

from typing import Optional

from wolfsoftware.notify import error_message


def string_to_bytes(s: str) -> bytes:
    """
    Convert a string to bytes using UTF-8 encoding.

    Arguments:
        s (str): The input string.

    Returns:
        bytes: The encoded bytes.
    """
    return s.encode('utf-8')


def bytes_to_string(b: bytes) -> str:
    """
    Convert bytes to a string using UTF-8 decoding, ignoring errors.

    Arguments:
        b (bytes): The input bytes.

    Returns:
        str: The decoded string.
    """
    return b.decode('utf-8', errors='ignore')


def bytes_to_int(b: bytes) -> int:
    """
    Convert bytes to an integer using big-endian byte order.

    Arguments:
        b (bytes): The input bytes.

    Returns:
        int: The resulting integer.
    """
    return int.from_bytes(b, 'big')


def int_to_bytes(n: int, length: int) -> bytes:
    """
    Convert an integer to bytes using big-endian byte order.

    Arguments:
        n (int): The input integer.
        length (int): The length of the resulting byte sequence.

    Returns:
        bytes: The resulting bytes.
    """
    return n.to_bytes(length, 'big')


def string_to_int(s: str) -> int:
    """
    Convert a string to an integer by encoding it to bytes first.

    Arguments:
        s (str): The input string.

    Returns:
        int: The resulting integer.
    """
    return bytes_to_int(string_to_bytes(s))


def int_to_string(n: int, original_length: int) -> str:
    """
    Convert an integer to a string by converting it to bytes first.

    Arguments:
        n (int): The input integer.
        original_length (int): The original length of the string in bytes.

    Returns:
        str: The resulting string.
    """
    b: bytes = int_to_bytes(n, original_length)
    return bytes_to_string(b)


def read_secret_from_file(file_path: str) -> str:
    """
    Read a secret from a file.

    Arguments:
        file_path (str): The path to the file containing the secret.

    Returns:
        str: The secret read from the file.
    """
    if not os.path.exists(file_path):
        print(error_message(f"The file {file_path} does not exist."))
        sys.exit(1)

    with open(file_path, 'r', encoding='UTF-8') as file:
        return file.read().strip()


def read_share_from_file(file_path: str) -> tuple:
    """
    Read a share from a file and convert it to a tuple of integers.

    Arguments:
        file_path (str): The path to the file containing the share.

    Returns:
        tuple: The share read from the file as a tuple of integers.
    """
    if not os.path.exists(file_path):
        print(error_message(f"The file {file_path} does not exist."))
        sys.exit(1)

    with open(file_path, 'r', encoding='UTF-8') as file:
        return tuple(map(int, file.read().strip().split(',')))


def write_shares_to_files(shares: list, output: bool, directory: Optional[str] = None) -> None:
    """
    Write shares to files or print them to the output.

    Arguments:
        shares (list): The list of shares to write.
        output (bool): Whether to print the shares to the output.
        directory (Optional[str]): The directory to write the shares to. If None, shares are written to the current directory.
    """
    if output:
        for share in shares:
            print(f'Share: {share[0]},{share[1]}')
    else:
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        for i, share in enumerate(shares, 1):
            share_file: str = os.path.join(directory, f'share-{i}.txt') if directory else f'share-{i}.txt'
            with open(share_file, 'w', encoding='UTF-8') as f:
                f.write(f'{share[0]},{share[1]}')
            print(f'Share {i} written to {share_file}')
