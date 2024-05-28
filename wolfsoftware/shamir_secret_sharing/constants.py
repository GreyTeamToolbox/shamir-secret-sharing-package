"""
Constants used in the Shamir's Secret Sharing implementation.

This module defines constants that are used throughout the Shamir's Secret Sharing scheme,
including a fixed large prime number and the maximum allowed length for a secret.
"""

# A fixed large prime number (>32768-bit prime)
FIXED_LARGE_PRIME = 2**32768 - 2**32704 + 2**7680 * ((2**32255 - 1) // 2**31) + 1

MAX_SECRET_LENGTH = 4096  # Maximum length in bytes for a secret
