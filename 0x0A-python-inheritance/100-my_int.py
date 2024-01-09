#!/usr/bin/python3
"""MyInt class that inherits from int."""


class MyInt(int):
    """MyInt class body"""

    def __eq__(self, value):
        """Override == opeartor with !=."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with ==."""
        return self.real == value
