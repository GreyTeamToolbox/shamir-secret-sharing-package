"""
This module defines global constants and retrieves the version information for the application.

This module sets up global constants used for the argument parser configuration and retrieves the version
information of the application package using the importlib.metadata module. If the package is not found,
the version is set to 'unknown'.
"""

import importlib.metadata

try:
    version: str = importlib.metadata.version('wolfsoftware.shamir_secret_sharing')
except importlib.metadata.PackageNotFoundError:
    version = 'unknown'

ARG_PARSER_PROG_NAME: str = "shamir-secret-sharing"
ARG_PARSER_DESCRIPTION: str = "Shamir\'s Secret Sharing CLI"
ARG_PARSER_EPILOG: str = "The Epilog goes here"

VERSION_STRING: str = f"Current version of {ARG_PARSER_PROG_NAME} is v{version}"
