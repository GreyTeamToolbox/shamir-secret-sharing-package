"""
Mathematical functions for Shamir's Secret Sharing.

This module provides utility functions for polynomial evaluations, coefficient generation, and Lagrange interpolation
used in Shamir's Secret Sharing scheme.
"""
from typing import List
import random
from functools import reduce


def polynomial(x: int, coefficients: list) -> int:
    """
    Evaluate a polynomial at a given point x.

    Arguments:
        x (int): The point at which to evaluate the polynomial.
        coefficients (list): The coefficients of the polynomial.

    Returns:
        int: The result of the polynomial evaluation.
    """
    return sum(coeff * x**i for i, coeff in enumerate(coefficients))


def generate_coefficients(secret: int, threshold: int) -> list:
    """
    Generate random coefficients for the polynomial, with the secret as the constant term.

    Arguments:
        secret (int): The secret to be shared, used as the constant term of the polynomial.
        threshold (int): The minimum number of shares required to reconstruct the secret.

    Returns:
        list: A list of coefficients for the polynomial.
    """
    coefficients: List[int] = [secret] + [random.SystemRandom().randint(0, 2**32) for _ in range(threshold - 1)]
    return coefficients


def lagrange_interpolation(x: int, shares: list, prime: int) -> int:
    """
    Perform Lagrange interpolation to reconstruct the secret.

    Arguments:
        x (int): The point at which to evaluate the polynomial (typically 0 for reconstructing the secret).
        shares (list): The list of shares, each a tuple containing the share index and value.
        prime (int): The prime number used in the sharing scheme.

    Returns:
        int: The reconstructed secret as an integer.
    """
    def _basis(j: int) -> int:
        """
        Calculate the Lagrange basis polynomial at index j.

        Arguments:
            j (int): The index of the basis polynomial.

        Returns:
            int: The value of the basis polynomial.
        """
        xj, _ = shares[j]

        def _product(m: int) -> int:
            """
            Calculate the product term for the basis polynomial.

            Arguments:
                m (int): The current index in the product calculation.

            Returns:
                int: The product term value.
            """
            xm, _ = shares[m]
            if m != j:
                # Calculate the product term for Lagrange interpolation
                return (x - xm) * pow(xj - xm, -1, prime) % prime
            return 1
        # Reduce the product over all shares to get the basis polynomial value
        return reduce(lambda acc, m: acc * _product(m) % prime, range(len(shares)), 1)

    # Sum up all the Lagrange basis polynomials multiplied by their corresponding y-values
    return sum(yj * _basis(j) % prime for j, (xj, yj) in enumerate(shares)) % prime
