"""
Main module for the wolfsoftware.shamir_secret_sharing package.

This module initializes the package by importing essential functions and constants from submodules,
sets the package version, and defines the `__all__` list for public API exposure.
"""

import importlib.metadata

from .constants import FIXED_LARGE_PRIME, MAX_SECRET_LENGTH
from .create import create_shares, create_actual_shares
from .utils import (
    string_to_bytes,
    bytes_to_string,
    bytes_to_int,
    int_to_bytes,
    string_to_int,
    int_to_string,
    read_secret_from_file,
    read_share_from_file,
    write_shares_to_files
)
from .reconstruct import reconstruct_secret

try:
    __version__ = importlib.metadata.version('wolfsoftware.shamir_secret_sharing')
except importlib.metadata.PackageNotFoundError:
    __version__ = 'unknown'

__all__ = [
    'string_to_bytes',
    'bytes_to_string',
    'bytes_to_int',
    'int_to_bytes',
    'string_to_int',
    'int_to_string',
    'read_secret_from_file',
    'read_share_from_file',
    'write_shares_to_files',
    'create_shares',
    'create_actual_shares',
    'reconstruct_secret',
    'FIXED_LARGE_PRIME',
    'MAX_SECRET_LENGTH'
]
