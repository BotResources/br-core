"""
Custom exceptions
"""

class BrCoreError(Exception):
    """Base exception for a br-core errors."""


class CriticResponseParsingError(Exception):
    """Raised when the Critic Response cannot be parsed"""