"""
This file is for custom exception
"""

class MathError(Exception):
    """Base class for all math-related exceptions."""
    pass


class EmptyDataError(MathError):
    """Raised when attempting to compute on an empty dataset."""

    def __init__(self, operation: str, message: str = "Empty dataset provided"):
        self.operation = operation
        self.message = message
        super().__init__(f"{self.message} in {self.operation}")
