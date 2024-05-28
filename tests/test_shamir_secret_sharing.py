"""
Unit tests for the shamir_secret_sharing package from wolfsoftware.

This module contains various test functions to verify the functionality of the shamir_secret_sharing package.
It includes tests for converting between data types, reading and writing secrets and shares from/to files,
creating and reconstructing shares, and handling edge cases such as excessively long secrets.
"""

from typing import Any, Literal, Optional

import importlib.metadata

import pytest

from wolfsoftware.shamir_secret_sharing import (
    string_to_bytes,
    bytes_to_string,
    bytes_to_int,
    int_to_bytes,
    string_to_int,
    int_to_string,
    read_secret_from_file,
    read_share_from_file,
    write_shares_to_files,
    create_actual_shares,
    reconstruct_secret,
    FIXED_LARGE_PRIME,
    MAX_SECRET_LENGTH
)


def test_version() -> None:
    """
    Test to ensure the version of the package is set and not 'unknown'.

    This test retrieves the version of the package using importlib.metadata and asserts that the version
    is not None and not 'unknown'.
    """
    version: Optional[str] = None

    try:
        version = importlib.metadata.version('wolfsoftware.shamir_secret_sharing')
    except importlib.metadata.PackageNotFoundError:
        version = None

    assert version is not None, "Version should be set"  # nosec: B101
    assert version != 'unknown', f"Expected version, but got {version}"  # nosec: B101


def test_string_to_bytes() -> None:
    """
    Test the string_to_bytes function.

    This test checks that the string_to_bytes function correctly converts a string to bytes.
    """
    assert string_to_bytes("test") == b"test"  # nosec: B101


def test_bytes_to_string() -> None:
    """
    Test the bytes_to_string function.

    This test checks that the bytes_to_string function correctly converts bytes to a string.
    """
    assert bytes_to_string(b"test") == "test"  # nosec: B101


def test_bytes_to_int() -> None:
    """
    Test the bytes_to_int function.

    This test checks that the bytes_to_int function correctly converts bytes to an integer.
    """
    assert bytes_to_int(b"test") == 1952805748  # nosec: B101


def test_int_to_bytes() -> None:
    """
    Test the int_to_bytes function.

    This test checks that the int_to_bytes function correctly converts an integer to bytes.
    """
    assert int_to_bytes(1952805748, 4) == b"test"  # nosec: B101


def test_string_to_int() -> None:
    """
    Test the string_to_int function.

    This test checks that the string_to_int function correctly converts a string to an integer.
    """
    assert string_to_int("test") == 1952805748  # nosec: B101


def test_int_to_string() -> None:
    """
    Test the int_to_string function.

    This test checks that the int_to_string function correctly converts an integer to a string.
    """
    assert int_to_string(1952805748, 4) == "test"  # nosec: B101


def test_read_secret_from_file(tmp_path) -> None:
    """
    Test the read_secret_from_file function.

    This test checks that the read_secret_from_file function correctly reads a secret from a file.
    """
    secret = "This is a test secret"  # nosec: B105
    secret_file: Any = tmp_path / "secret.txt"
    secret_file.write_text(secret)
    read_secret: str = read_secret_from_file(secret_file)
    assert read_secret == secret  # nosec: B101


def test_read_share_from_file(tmp_path) -> None:
    """
    Test the read_share_from_file function.

    This test checks that the read_share_from_file function correctly reads a share from a file.
    """
    share: tuple[Literal[1], Literal[1234567890]] = (1, 1234567890)
    share_file: Any = tmp_path / "share-1.txt"
    share_file.write_text(f"{share[0]},{share[1]}")
    read_share: tuple[int, ...] = read_share_from_file(share_file)
    assert read_share == share  # nosec: B101


def test_write_shares_to_files(tmp_path, capsys) -> None:
    """
    Test the write_shares_to_files function.

    This test checks that the write_shares_to_files function correctly writes shares to files
    and optionally prints them to the output.
    """
    shares: list = [(1, 1234567890), (2, 987654321)]
    output_dir: Any = tmp_path / "output"
    output_dir.mkdir()

    # Test writing to files
    write_shares_to_files(shares, output=False, directory=output_dir)
    for i, (index, value) in enumerate(shares, 1):
        share_file: Any = output_dir / f"share-{i}.txt"
        with open(share_file, 'r', encoding='UTF-8') as f:
            content: str = f.read().strip()
        assert content == f"{index},{value}"  # nosec: B101

    # Test printing to output
    write_shares_to_files(shares, output=True)
    captured: Any = capsys.readouterr()
    assert "Share: 1,1234567890" in captured.out  # nosec: B101
    assert "Share: 2,987654321" in captured.out  # nosec: B101


def test_create_and_reconstruct_shares() -> None:
    """
    Test the create_actual_shares and reconstruct_secret functions.

    This test checks that shares can be created from a secret and then correctly used to reconstruct
    the original secret.
    """
    secret = "mySecretPassword1234567890"  # nosec: B105
    total_shares = 5
    threshold = 3

    # Ensure secret length is within the limit
    assert len(secret) <= MAX_SECRET_LENGTH  # nosec: B101

    shares: list[tuple[int, int]] = create_actual_shares(secret, total_shares, threshold)
    assert len(shares) == total_shares  # nosec: B101

    prime: Any = FIXED_LARGE_PRIME  # Use the sufficiently large fixed prime number
    original_length: int = len(secret)
    reconstructed_secret_int: Any = reconstruct_secret(shares[:threshold], prime)
    reconstructed_secret_bytes: Any = int_to_bytes(reconstructed_secret_int, original_length)
    reconstructed_secret: Any = bytes_to_string(reconstructed_secret_bytes)
    assert reconstructed_secret == secret  # nosec: B101


def test_secret_too_long() -> None:
    """
    Test handling of excessively long secrets.

    This test checks that an appropriate error is raised when attempting to create shares from
    a secret that exceeds the maximum allowed length.
    """
    secret: str = "a" * (MAX_SECRET_LENGTH + 1)  # nosec: B101
    total_shares = 5
    threshold = 3

    with pytest.raises(ValueError, match=f"Secret is too long. Maximum length is {MAX_SECRET_LENGTH} bytes."):
        create_actual_shares(secret, total_shares, threshold)  # nosec: B101


def test_multi_line_secret() -> None:
    """
    Test handling of multi-line secrets.

    This test checks that multi-line secrets can be correctly shared and reconstructed.
    """
    secret = (
        """This is a multi-line secret.
        It spans multiple lines.
        Shamir's Secret Sharing can handle this."""
    )   # nosec: B105
    total_shares = 5
    threshold = 3

    shares: list[tuple[int, int]] = create_actual_shares(secret, total_shares, threshold)
    assert len(shares) == total_shares  # nosec: B101

    secret_bytes: bytes = string_to_bytes(secret)
    prime: Any = FIXED_LARGE_PRIME  # Use the sufficiently large fixed prime number
    original_length: int = len(secret_bytes)
    reconstructed_secret_int: Any = reconstruct_secret(shares[:threshold], prime)
    reconstructed_secret_bytes: Any = int_to_bytes(reconstructed_secret_int, original_length)
    reconstructed_secret: Any = bytes_to_string(reconstructed_secret_bytes)
    assert reconstructed_secret == secret  # nosec: B101
