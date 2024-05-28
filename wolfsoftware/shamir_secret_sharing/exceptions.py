"""
This module defines a custom exception class for the application.

This module provides a CustomException class that extends the built-in Exception class. It can be used to
raise and handle application-specific exceptions in a more descriptive manner.
"""


class CustomException(Exception):
    """
    A custom exception class for application-specific errors.

    This class extends the built-in Exception class to provide a custom exception type for handling
    specific errors within the application. It allows for more descriptive and specific error handling.

    Arguments:
        Exception (class): The base exception class from which this custom exception inherits.
    """
